from django.db import models
from django.contrib.auth.models import User


# Create your models here.
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
    

class Quiz(models.Model):
    name = models.CharField(max_length=255, default='New Quiz')
    description = models.TextField(null=True, blank=True)
    # Add any other fields you need for your quiz

    def __str__(self):
        return self.name


class Question(models.Model):
    quiz = models.ForeignKey(to=Quiz, on_delete=models.CASCADE, 
        related_name='questions', null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    # Add any other fields you need for your questions
    
    def __str__(self):
        return self.text

class Choice(models.Model):
    question = models.ForeignKey(to=Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)
    # Add any other fields you need for choices
    
    def __str__(self):
        return f'{self.question}, {self.text}, {self.is_correct}' 


class Video(models.Model):
    name = models.CharField(max_length=122, default='New Video')
    url = models.CharField(max_length=122, default='New Video')
    gist = models.CharField(max_length=122, default='New Gist')
    comments = models.ManyToManyField(to=Comment, default=None)
    quiz = models.OneToOneField(to=Quiz, on_delete=models.CASCADE, null=True, blank=True)
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
    learners = models.IntegerField(default=0)
    videos = models.ManyToManyField(to=Video, default='No Videos')
    quiz = models.OneToOneField(to=Quiz, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class Learner(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    courses = models.ManyToManyField(to=Course)
    subscription_end = models.DateField(null=True)

    def __str__(self):
        return self.user.username



    



