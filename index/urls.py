from . import views
from django.urls import path
from django.urls import include

app_name = 'index'

urlpatterns = [
    path(route='', view=views.home, name='home'),
    path(route='back/', view=views.back, name='back'),
    path(route='school/', view=include('school.urls'), name='school'),
    path(route='feedback/', view=views.feedback, name='feedback'),
    path(route='terms_of_service', view=views.termsOfService, name='terms_of_service'),
    path(route='privacy_policy', view=views.privacyPolicy, name='privacy_policy'),
    path(route='portfolio_details/<int:id>', view=views.portfolio_details, name='portfolio_details')
]