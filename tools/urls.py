from django.urls import path
from . import views

app_name = 'tools'

urlpatterns = [
    path(route='transcriber/upload/', view=views.upload_file, name='upload_transcribe_file'),
    path(route='transcriber/download/<int:pk>/<str:option>/', view=views.download_transcription, name='download_transcription'),
    path(route='note/add_note/', view=views.add_note, name='add_note'),
    path(route='note/delete_note/<int:id>', view=views.delete_note, name='delete_note'),
    path(route='note/one_note/<int:id>', view=views.one_note, name='one_note'),
]
