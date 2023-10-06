import os
import assemblyai as aai
from .models import Note
from .models import Devotion
from langchain.llms import OpenAI
from .models import Transcription
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from .forms import DevotionForm, AudioUploadForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, HttpResponse
from .forms import AudioUploadForm, TranscriptionOptionsForm, DevotionForm


def transcribe(audio_file):
    aai.settings.api_key = f"3282ce6eca0a47519f6f69dbbaa38da6"
    transcription = Transcription(audio_file=audio_file)
    transcription.save()

    transcriber = aai.Transcriber()

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

    return transcription


@login_required(login_url='accounts:signin')
def generateDevotion(request):
    os.environ["OPENAI_API_KEY"] = "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"
    devotion_form = DevotionForm()
    audio_form = AudioUploadForm()
    if request.method == 'POST':
        devotion_form = DevotionForm(request.POST)
        audio_form = AudioUploadForm(request.POST, request.FILES)

        if audio_form.is_valid() and devotion_form.is_valid():
            audio_file = audio_form.cleaned_data['audio_file']
            scripture = devotion_form.cleaned_data['scripture']

            transcription = transcribe(audio_file=audio_file)
            
            llm = OpenAI(temperature=0, model='gpt-3.5-turbo')

            devotion_prompt = '''
            I would like you to write me a "devotion" based on {scripture} and this summary below
            {summary} 
            I have two examples of "devotion" that I want you to learn from. The first one is as below

            #IndisputableGeneration
            Tuesday 26th September 2023

            YOUR DAILY PRAYER IGNITE 
            BY Ap. Samuel Muyita

            John 12:3 Then took Mary a pound of ointment of spikenard, very costly, and anointed the feet of Jesus, and wiped his feet with her hair: and the house was filled with the odour of the ointment.

            SPENDING ON JESUS 

            It’s in the ways of God that He only trusts you with what you can give Him back. Anything you aren’t ready to spend on Him, you aren’t ready to receive!

            The scriptures are clear, “For where your treasure is, there will your heart be also” Matthew 6:21. Whenever our hearts are fully given to Him, our treasures too will be!

            In our theme scripture, we see Mary, taking something very costly and spending it on Jesus! Judas called it wasting, but Jesus saw it as love! She added on that and laid her crown of glory (hair) at the feet of Jesus to wipe His feet!

            Whatever we spend on behalf of God is not wasted, but it’s a statement to heaven that we understand where our treasure is, and there our hearts also will be!

            Your heart will be tested, God will try you with a little of what you think you are ready for, and oftentimes, many eyes are blinded by the hand of God that they miss His heart. If you can’t spend on behalf of the Kingdom, you’re not yet ready for abundance.

            PRAYER POINT 
            You have the wisdom to lay down anything for the sake of the Kingdom. You understand the responsibility of wealth and as God multiplies what is upon your life, your heart stays fixed on God as your ultimate treasure. Hallelujah

            The second example is as below

            #IndisputableGeneration
            Friday 29th September 2023

            YOUR DAILY PRAYER IGNITE 
            BY Ap. Samuel Muyita

            Proverbs 4:23 (NIV): "Above all else, guard your heart, for everything you do flows from it."

            GUARDIANS OF THE HEART

            In the treasury of wisdom found in Proverbs, we are given this profound and vital command: "Above all else, guard your heart." It's a directive that carries immense significance because our hearts are the wellspring of our lives, the source from which everything flows.

            Our hearts are not merely the physical organ that pumps blood through our bodies; they are the seat of our emotions, desires, and intentions. Our thoughts, words, and actions all emanate from the condition of our hearts.

            Just as a vigilant guard protects a fortress, we are called to be guardians of our hearts. Why? Because the state of our hearts profoundly impacts the course of our lives. When our hearts are filled with love, compassion, and righteousness, our actions reflect these qualities. Conversely, a heart tainted by bitterness, anger, or envy can lead us down a destructive path.

            In the spiritual journey, guarding our hearts means cultivating a heart that is aligned with God's Word. It means regularly examining our hearts, seeking forgiveness and healing when necessary, and filling our hearts with the love, grace, and truth of Christ.

            So, today, let us pray together:

            PRAYER POINT
            Heavenly Father, we come before you with hearts open and vulnerable. We recognize the importance of guarding our hearts above all else. Please help us to keep our hearts pure and aligned with your will. Grant us the wisdom and discernment to nurture a heart that overflows with love, kindness, and righteousness. May everything we do flow from a heart devoted to you. In Jesus' name, we pray. Amen.

            Please develop your devotion in the similar way the examples were developed.
            '''

            devotion_prompt_template = PromptTemplate(
                input_variables=["scripture", 'summary'],
                template = devotion_prompt,
            )

            # llm_chain = LLMChain(llm=llm, prompt=devotion_prompt_template)
            # res_devotion = llm_chain.run(scripture=scripture, 
            #                              summary=transcription.summary_text)

            res_devotion = transcription.summary_text

            # devotion = Devotion(scripture=scripture, 
            #                     detail=res_devotion, 
            #                     user=request.user)
            # devotion.save()

            template_name = 'tools/devotion_out.html'
            return render(request=request,
                          template_name=template_name,
                          context={'devotion': res_devotion,})
    else:
        return render(request=request,
                      template_name='tools/devotion.html',
                      context={'devotion_form': devotion_form, 
                               'audio_form': audio_form}
                      )
    
def downloadDevotion(request, pk):
    import io
    from reportlab.pdfgen import canvas

    devotion = Devotion.objects.get(pk=pk)
    pdf_file = io.BytesIO()
    canvas = canvas.Canvas(pdf_file)
    canvas.setFont("Helvetica", 12)
    canvas.drawString(10, 10, devotion.detail)
    canvas.showPage()
    canvas.save()

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="devotion.pdf"'

    response.write(pdf_file.getvalue())

    pdf_file.close()

    return response

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

