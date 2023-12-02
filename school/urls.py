from django.urls import path
from . import views

app_name = 'school'

urlpatterns = [
    path(route='', view=views.browse, name='browse'),
    path(route='profile', view=views.profile, name='profile'),
    path(route='update-profile', view=views.updateProfile, name='update_profile'),
    path(route='search-courses/', view=views.searchCourses, name='search_courses'),
    path(route='comment/<int:id>', view=views.comment, name='comment'),
    path(route='course-details/<int:id>', view=views.course_details, name='course_details'),
    path(route='view-quiz/<int:quiz_id>/', view=views.view_quiz, name='view_quiz'),
    path(route='submit-quiz/<int:quiz_id>/', view=views.submit_quiz, name='submit_quiz'),
    path(route='download-learning-material/<int:id>', view=views.downloadLearningMaterial, name='download_learning_material'),
]