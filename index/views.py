from .models import TermOfService
from .models import PrivacyPolicy
from django.shortcuts import render, redirect
from .forms import FeedbackForm
from django.core.mail import send_mail


# Create your views here.
def home(request):
    
    context = {'form': FeedbackForm}
    template_name = 'index/index.html'
    return render(request=request, 
                  template_name=template_name, 
                  context=context)

def back(request):
    return redirect(request.META.get('HTTP_REFERER'))

def feedback(request):
    context = {}
    try:
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feed = form.save()

            send_mail(
                subject=feed.subject,
                message=f'{feed.message}. \n From: \n {feed.name} \n {feed.email}',
                from_email='datasideaofficial@gmail.com',
                recipient_list=['datasideaofficial@gmail.com','jumashafara0@gmail.com'],
                auth_password='sjkt gmrm xihb iidk',
                
                fail_silently=False
            )
            
            context['message'] = f'Thanks for contacting us, we will get back to you as soon as possible.'
        else:
            return redirect(to='/#contactFrom')
    except Exception as e:
        context['message'] = f'Something went wrong. Please try again later. {e}'

    template_name='components/message.html'
    return render(request=request, template_name=template_name, context=context)

def termsOfService(request):
    terms_of_service = TermOfService.objects.all()
    context = {'terms_of_service':terms_of_service}
    
    template_name='index/terms_of_service.html'
    return render(request=request, template_name=template_name, context=context)

def privacyPolicy(request):
    privacy_policy = PrivacyPolicy.objects.all()
    context = {'privacy_policy':privacy_policy}
    
    template_name='index/privacy_policy.html'
    return render(request=request, template_name=template_name, context=context)

def notAllowed(request):
    context = {'message': 'You are not allowed to access this page, contact admin for help.'}
    template_name = 'components/message.html'
    return render(request=request, template_name=template_name, context=context)

def paidFeature(request):
    context = {'message': 'This is a paid feature, however, a trial period can be granted, please contact admin for more information.'}
    template_name = 'components/message.html'
    return render(request=request, template_name=template_name, context=context)

def sitemap(request):
    template_name = 'index/sitemap.xml'
    return render(request=request, template_name=template_name)

def robots(request):
    template_name = 'index/robots.txt'
    return render(request=request, template_name=template_name)

def ads(request):
    template_name = 'index/ads.txt'
    return render(request=request, template_name=template_name)