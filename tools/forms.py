from django import forms

TRANSCRIPT_OPTIONS = [
    ('transcript', 'Transcribe'),
    ('summary', 'Summarize'),
]

class AudioUploadForm(forms.Form):
    audio_file = forms.FileField(
        label='Select an audio file (max size: 25MB)',
        required=True,
        widget=forms.ClearableFileInput(attrs={'accept': 'audio/*'}),
    )

class TranscriptionOptionsForm(forms.Form):
    transcript_option = forms.ChoiceField(
        label='Select Transcription Choice (Optional)',
        choices=TRANSCRIPT_OPTIONS,
        required=False,
        widget=forms.RadioSelect,
    )

class DevotionForm(forms.Form):
    scripture = forms.CharField(
        label='Scripture',
        max_length=255,
        required=False,
    )
