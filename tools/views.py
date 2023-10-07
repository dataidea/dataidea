import os
import assemblyai as aai
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from .models import Note, Devotion, Transcription, Secret
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, HttpResponse
from .forms import AudioUploadForm, TranscriptionOptionsForm, DevotionForm


def transcribe(audio_file):
    try:
        aai.settings.api_key = f"{Secret.objects.get(label='AssemblyAi').value}"
        transcription = Transcription(audio_file=audio_file)
        transcription.save()

        transcriber = aai.Transcriber()

    # Summarize the audio file
    
        transcript = transcriber.transcribe(
            data=transcription.audio_file.path,
            config=aai.TranscriptionConfig(
                summarization=True,
                summary_model=aai.SummarizationModel.informative,
                summary_type=aai.SummarizationType.bullets)
        )

        transcription.summary_text = transcript.summary
        transcription.transcription_text = transcript.text
        transcription.save()

    except:
        return None

    return transcription


def askOpenAi(prompt, scripture, summary):
    try:
        os.environ["OPENAI_API_KEY"] = Secret.objects.get(label='OpenAi').value

        llm = OpenAI(temperature=0.9)
        prompt_template = PromptTemplate(
                    input_variables=['scripture', 'summary'],
                    template = prompt,
                )
        
        llm_chain = LLMChain(llm=llm, prompt=prompt_template)
        res_devotion = llm_chain.run(scripture=scripture, 
                                    summary=summary)
    except:
        res_devotion = 'Error generating devotion'

    return res_devotion.strip()


@login_required(login_url='accounts:signin')
def generateDevotion(request):
    devotion_form = DevotionForm()
    audio_form = AudioUploadForm()
    if request.method == 'POST':
        devotion_form = DevotionForm(request.POST)
        audio_form = AudioUploadForm(request.POST, request.FILES)

        if audio_form.is_valid() and devotion_form.is_valid():
            audio_file = audio_form.cleaned_data['audio_file']
            scripture = devotion_form.cleaned_data['scripture']

            transcription = transcribe(audio_file=audio_file)

            if transcription:
                text = transcription.transcription_text
                summary = transcription.summary_text
            else:
                text = 'No audio was provide for transcription'
                summary = 'No transcript to summarize'
            
            if scripture == '':
               return render(request=request,
                          template_name='tools/devotion_out.html',
                          context={'devotion': 'No Scripture Provided',
                                   'summary': summary,
                                   'text':text,
                                   'scripture': 'No Scripture Provided'}
                                   )
            else:
                devotion_prompt =  '''I would like you to write me a "devotion" based on {scripture}, 
                                    and this summary {summary} if its found.
                                    '''
                ai_res_devotion = askOpenAi(prompt=devotion_prompt,
                                            scripture=scripture,
                                            summary=summary
                                            )
                devotion = Devotion(scripture=scripture, 
                                    detail=ai_res_devotion, 
                                    user=request.user)
                devotion.save()

            return render(request=request,
                          template_name='tools/devotion_out.html',
                          context={'devotion': ai_res_devotion,
                                   'summary': summary,
                                   'text':text,
                                   'scripture': scripture}
                                   )
    else:
        return render(request=request,
                      template_name='tools/devotion.html',
                      context={'devotion_form': devotion_form, 
                               'audio_form': audio_form}
                      )


@login_required(login_url='accounts:signin')
def uploadFile(request):
    if request.method == 'POST':
        audio_form = AudioUploadForm(request.POST, request.FILES)
        options_form = TranscriptionOptionsForm(request.POST)

        if audio_form.is_valid() and options_form.is_valid():
            audio_file = audio_form.cleaned_data['audio_file']
            transcript_option = options_form.cleaned_data['transcript_option']
            
            transcription = transcribe(audio_file)

            return redirect(to='download_transcription',
                            pk=transcription.pk,
                            option='text' if transcript_option == 'text' else 'summary')

    else:
        audio_form = AudioUploadForm()
        options_form = TranscriptionOptionsForm()

    return render(request, 'tools/upload.html', {'audio_form': audio_form, 'options_form': options_form})

def downloadTranscription(request, pk, option):
    transcription = Transcription.objects.get(pk=pk)
    response = HttpResponse(content_type='text/plain')

    if option == 'text':
        response['Content-Disposition'] = f'attachment; filename="transcription_text.txt"'
        response.write(transcription.transcription_text)
    else:
        response['Content-Disposition'] = f'attachment; filename="transcription_summary.txt"'
        response.write(transcription.summary_text)
    return response


# Notes Section
@login_required(login_url='accounts:signin')
def addNote(request):
    if request.method == 'POST':
        title = request.POST.get(key='title')
        detail = request.POST.get(key='detail')
        note = Note(title=title, detail=detail, user=request.user)
        note.save()
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        user_notes = Note.objects.filter(user = request.user)
        template_name = 'tools/notes.html'
        context = {'notes': user_notes}
        return render(request=request, template_name=template_name, context=context)

@login_required(login_url='accounts:signin')
def oneNote(request, id):
    try:
        note = Note.objects.get(id=id)
        if request.method == 'POST':
            title = request.POST.get(key='title')
            detail = request.POST.get(key='detail')
            note = Note(title=title, detail=detail, user=request.user)
            note.save()
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            template_name = 'tools/note_detail.html'
            context = {'note': note}
            return render(request=request, template_name=template_name, context=context)
    except Note.DoesNotExist as dne:
        context = {'state': 'danger', 'message': 'Note does not exist!'}
        template_name = 'components/message.html'
        return render(request=request, template_name=template_name, context=context)
    except Exception as e:
        context = {'state': 'danger', 'message': 'An error occured while trying to fetch the note'}
        template_name = 'components/message.html'
        return render(request=request, template_name=template_name, context=context)


@login_required(login_url='accounts:signin')
def deleteNote(request, id):
    try:
        note = Note.objects.get(id=id)
        note.delete()
        return redirect(to='tools:add_note')
    except Note.DoesNotExist as dne:
        context = {'state': 'warning', 'message': 'Note does not exist!'}
        template_name = 'components/message.html'
        return render(request=request, template_name=template_name, context=context)
    except Exception as e:
        context = {'state': 'warning', 'message': 'An error occured while trying to delete the note'}
        template_name = 'components/message.html'
        return render(request=request, template_name=template_name, context=context)

