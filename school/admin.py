from .models import Quiz
from .models import Tutor
from .models import Video
from .models import Course
from .models import Choice
from .models import Learner
from .models import Comment
from .models import Question
from .models import Organization
from django.contrib import admin


# admin models
class CourseAdmin(admin.ModelAdmin):
    filter_horizontal = ['tutors', 'videos']


class VideoAdmin(admin.ModelAdmin):
    filter_horizontal = []


    

# Register your models here.
admin.site.register(model_or_iterable=Course, admin_class=CourseAdmin)
admin.site.register(model_or_iterable=[Choice, Comment,Organization, Quiz, Tutor, Video, Learner, Question])

