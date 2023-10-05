from django.urls import path
from . import views

app_name = 'profiles'

urlpatterns = [
    path(route='jumashafara', view=views.jumaShafara, name='jumashafara')
]