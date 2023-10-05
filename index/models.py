from django.db import models

# Create your models here.
class Service(models.Model):
    icon = models.CharField(max_length=122, default='layer')
    color = models.CharField(max_length=22, default='#f5f5f5')
    name = models.CharField(max_length=122)
    description = models.TextField(default="One of our services")

    def __str__(self):
        return self.name

class Feature(models.Model):
    icon = models.CharField(max_length=122, default='layer' )
    name = models.CharField(max_length=122)
    description = models.TextField()

    def __str__(self):
        return self.name


class Testimonial(models.Model):
    name = models.CharField(max_length=122)
    image = models.ImageField(upload_to='testimonials')
    position = models.CharField(max_length=122)
    testimony = models.TextField()

    def __str__(self):
        return self.name


class Portfolio(models.Model):
    CATEGORIES = [('web', 'Web'), ('other', 'Other'), ('tutorial', 'Tutorial')]      
    name = models.CharField(max_length=122)
    image = models.ImageField(upload_to='portfolio')
    category = models.CharField(max_length=8, choices=CATEGORIES)
    client = models.CharField(max_length=50, default='Private')
    url = models.CharField(max_length=100, default='No url')
    date = models.DateField(null=True)
    description = models.TextField(default='No description')

    def __str__(self):
        return self.name
    

class Partner(models.Model):
    name = models.CharField(max_length=122, default='Partner')
    image = models.CharField(max_length=122, default='partner')
    url = models.CharField(max_length=100, default='No url')

    def __str__(self):
        return self.name
    

class Price(models.Model):
    name = models.CharField(max_length=122)
    price = models.CharField(max_length=122)
    service = models.ForeignKey(to=Service, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class FrequentlyAskedQuestion(models.Model):
    question = models.CharField(max_length=122)
    answer = models.TextField()

    def __str__(self):
        return self.question

class Contact(models.Model):
    icon = models.CharField(max_length=122, default='contact')
    name = models.CharField(max_length=122)
    contact = models.CharField(max_length=122)

    def __str__(self):
        return self.name
    
class CompanyInfo(models.Model):
    name = models.CharField(max_length=122, default='DataIdea')
    highlight = models.CharField(max_length=122, default='Better Digital Experience With DataIdea')
    description = models.TextField(default='We are a team of talented researchers and developers providing the best services by optimizing the latest tech')
    clients = models.IntegerField(default=5)
    projects = models.IntegerField(default=5)
    workers = models.IntegerField(default=5)
    hours_of_support = models.IntegerField(default=5)

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

    

