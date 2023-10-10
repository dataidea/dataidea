from django.urls import path
from . import views

app_name = 'tools'

urlpatterns = [
    path(route='transcriber/upload/', view=views.uploadFile, name='upload_transcribe_file'),
    path(route='transcriber/download/<int:pk>/<str:option>/', view=views.downloadTranscription, name='download_transcription'),
    path(route='note/add_note/', view=views.addNote, name='add_note'),
    path(route='note/delete_note/<int:id>', view=views.deleteNote, name='delete_note'),
    path(route='note/one_note/<int:id>', view=views.oneNote, name='one_note'),
]
