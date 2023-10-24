from django.contrib import admin
from .models import Note, Transcription, Secret

# Register your models here.
admin.site.register(model_or_iterable=[Note, Transcription, Secret])
