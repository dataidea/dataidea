from django.db import models

class Contact(models.Model):
    icon = models.CharField(max_length=122, default='contact')
    name = models.CharField(max_length=122)
    contact = models.CharField(max_length=122)

    def __str__(self):
        return self.name
    

class TermOfService(models.Model):
    name = models.CharField(max_length=122, default='Terms of Service')
    description = models.TextField(default='By using the services provided by Data Idea ("the Company"), you agree to comply with and be bound by the following Terms of Service ("TOS"). If you do not agree with these terms, please do not use our services.')

    def __str__(self):
        return self.name
    
class PrivacyPolicy(models.Model):
    name = models.CharField(max_length=122, default='Privacy Policy')
    description = models.TextField(default='By using the services provided by Data Idea ("the Company"), you agree to comply with and be bound by the following Privacy Policy ("Privacy Policy"). If you do not agree with these terms, please do not use our services.')

    def __str__(self):
        return self.name
    
class Feedback(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    subject = models.CharField(max_length=244)
    message = models.TextField()

    def __str__(self):
        return self.subject

    

