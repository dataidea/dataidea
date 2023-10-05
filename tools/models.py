from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Transcription(models.Model):
    audio_file = models.FileField(upload_to='audio_files/')
    transcription_text = models.TextField(blank=True)
    summary_text = models.TextField(blank=True)

    def __str__(self):
        return self.audio_file
    

class Note(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, default='Note Title')
    detail = models.TextField(default='Note Detail')
    date_created = models.DateField(auto_now=True)
    def __str__(self):
        return f'{self.user.username}, {self.title}'