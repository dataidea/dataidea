from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class LearnerProfile(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    display_picture = models.ImageField(upload_to='profiles/', default='profiles/profile.jpg')
    name = models.CharField(max_length=122, default='No name provided')
    info = models.CharField(max_length=122, default='')
    github = models.CharField(max_length=122, default='')
    linkedin = models.CharField(max_length=122, default='')
    other = models.CharField(max_length=122, default='')

    def __str__(self):
        return self.name


class Tutor(models.Model):
    name = models.CharField(max_length=122, default='New Tutor')
    info = models.CharField(max_length=122, default='New Tutor')

    def __str__(self):
        return self.name

class Organization(models.Model):
    name = models.CharField(max_length=122, default='DataIdea')
    url = models.CharField(max_length=122, default='dataidea.com')

    def __str__(self):
        return self.name


class Comment(models.Model):
    approved = models.BooleanField(default=False)
    comment = models.TextField(default='New Comment')
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, default=12)
    def __str__(self):
        return self.comment


class Queztion(models.Model):
    text = models.TextField(null=True, blank=True)
    # Add any other fields you need for your questions

    def __str__(self):
        return self.text
    

class Choize(models.Model):
    Queztion = models.ForeignKey(to=Queztion, on_delete=models.CASCADE, null=True, blank=True)
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)
    # Add any other fields you need for choices

    def __str__(self):
        return f'{self.question}, {self.text}, {self.is_correct}'

    

class Quizz(models.Model):
    name = models.CharField(max_length=255, default='New Quiz')
    description = models.TextField(null=True, blank=True)
    queztionz = models.ManyToManyField(to=Queztion, blank=True, null=True)
    # Add any other fields you need for your quiz

    def __str__(self):
        return self.name



class Video(models.Model):
    name = models.CharField(max_length=122, default='New Video')
    url = models.CharField(max_length=122, default='New Video')
    gist = models.CharField(max_length=122, default='New Gist')
    comments = models.ManyToManyField(to=Comment, default=None, blank=True)
    quiz = models.OneToOneField(to=Quizz, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.name


class LearningMaterial(models.Model):
    name = models.CharField(max_length=122, default='New Learning Material')
    file = models.FileField(upload_to='learning_materials/', default='learning_materials/default.pdf')

    def __str__(self):
        return self.name


class Course(models.Model):
    LEVELS = [('reception-1', 'Beginner'), ('reception-2', 'Intermediate'), ('reception-3', 'Advanced'), ('reception-4', 'Explorer'),]
    name = models.CharField(max_length=122, default='New Course')
    description = models.TextField(default='New Course')
    image = models.ImageField(upload_to='course_images/', default='images/default.jpg')
    organization = models.ForeignKey(to=Organization, default=0, on_delete=models.CASCADE)
    tutors = models.ManyToManyField(to=Tutor, default='Not Identified')
    url = models.CharField(max_length=122, default='No URLs provided attached')
    level = models.CharField(max_length=22, choices=LEVELS, default='reception-1')
    learning_materials = models.OneToOneField(to=LearningMaterial, on_delete=models.CASCADE, null=True, blank=True)
    videos = models.ManyToManyField(to=Video, default='No Videos')
    quiz = models.OneToOneField(to=Quizz, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name
    

class QuizScore(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(to=Quizz, on_delete=models.CASCADE, null=True, blank=True)
    score = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.user}, {self.quiz}, {self.score}'
    
    @classmethod
    def updateOrCreateScore(cls, user, quiz, score):
        try:
            quiz_score = cls.objects.get(user=user, quiz=quiz)
            quiz_score.score = score
            quiz_score.save()
        except cls.DoesNotExist:
            quiz_score = cls(user=user, quiz=quiz, score=score)
            quiz_score.save()
        return quiz_score






