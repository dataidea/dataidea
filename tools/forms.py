from django import forms

TRANSCRIPT_OPTIONS = [
    ('transcript', 'Transcript Only'),
    ('summary', 'Summary Only'),
]

class AudioUploadForm(forms.Form):
    audio_file = forms.FileField(
        label='Select an audio file (max size: 25MB)',
        required=True,
        widget=forms.ClearableFileInput(attrs={'accept': 'audio/*'}),
    )

class TranscriptionOptionsForm(forms.Form):
    transcript_option = forms.ChoiceField(
        label='Select Transcription Option',
        choices=TRANSCRIPT_OPTIONS,
        required=True,
        widget=forms.RadioSelect,
    )
