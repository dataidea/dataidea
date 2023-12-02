from .models import (QuizScore, Question, Quiz, 
                     Choice, Comment, Course, 
                     Organization, Tutor, Video, 
                     LearningMaterial, LearnerProfile)

from django.contrib import admin


# admin models
class CourseAdmin(admin.ModelAdmin):
    filter_horizontal = ['tutors', 'videos']


class VideoAdmin(admin.ModelAdmin):
    filter_horizontal = []


# Register your models here.
admin.site.register(model_or_iterable=Course, admin_class=CourseAdmin)
admin.site.register(model_or_iterable=[QuizScore, Choice, Comment,
                                       Organization, Quiz, Tutor, 
                                       Video, LearningMaterial, Question,
                                       LearnerProfile])

