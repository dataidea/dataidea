from django.urls import path
from . import views

app_name = 'school'

urlpatterns = [
    path(route='', view=views.browse, name='browse'),
    path(route='search_courses/', view=views.searchCourses, name='search_courses'),
    path(route='comment/<int:id>', view=views.comment, name='comment'),
    path(route='course-details/<int:id>', view=views.course_details, name='course_details'),
    path(route='quiz/<int:quiz_id>/', view=views.quiz_view, name='quiz'),

]