from .models import Note
from django.contrib import admin
from .models import Transcription

# Register your models here.
# class TranscriptionAdmin(admin.ModelAdmin):
#     list_display = []
admin.site.register(model_or_iterable=[Note, Transcription])
