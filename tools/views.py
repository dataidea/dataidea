import assemblyai as aai
from .models import Note
from .models import Transcription
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, HttpResponse
from .forms import AudioUploadForm, TranscriptionOptionsForm

aai.settings.api_key = f"3282ce6eca0a47519f6f69dbbaa38da6"

@login_required(login_url='accounts:signin')
def upload_file(request):
    if request.method == 'POST':
        audio_form = AudioUploadForm(request.POST, request.FILES)
        options_form = TranscriptionOptionsForm(request.POST)

        if audio_form.is_valid() and options_form.is_valid():
            audio_file = audio_form.cleaned_data['audio_file']
            transcript_option = options_form.cleaned_data['transcript_option']

            # Save the uploaded audio file
            transcription = Transcription(audio_file=audio_file)
            transcription.save()

            # Transcribe the audio file
            transcriber = aai.Transcriber()
            transcript = transcriber.transcribe(
            data=transcription.audio_file.path,
            config= aai.TranscriptionConfig(
                summarization= True,
                summary_model=aai.SummarizationModel.informative,
                summary_type=aai.SummarizationType.bullets
            ))

            transcription.summary_text = transcript.summary
            transcription.transcription_text = transcript.text
            # Save transcription
            transcription.save()


            return redirect(to='download_transcription',
                            pk=transcription.pk,
                            option='text' if transcript_option == 'text' else 'summary')




    else:
        audio_form = AudioUploadForm()
        options_form = TranscriptionOptionsForm()

    return render(request, 'tools/upload.html', {'audio_form': audio_form, 'options_form': options_form})

def download_transcription(request, pk, option):
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
def add_note(request):
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
def one_note(request, id):
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
def delete_note(request, id):
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
