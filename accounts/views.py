from django.db.models import Q
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth import logout
# from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from .forms import CustomAuthenticationForm
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.


def signin(request):
    if request.method == "POST":
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request=request, user=user)
            if 'next' in request.POST:
                return redirect(to=request.POST.get('next'))
            else:
                return redirect(to='/')
        else:
            error = 'Please enter correct username and password. Click "Lets sign you up" if you dont have an account.'
            template_name = 'accounts/signin.html'
            context = {'form': CustomAuthenticationForm()}
            return render(request, template_name=template_name, context=context)
    else:
        context = {}
        if 'next' in request.GET:
            context['message'] = 'You should be logged in with and account to see this page'

        template_name = 'accounts/signin.html'
        context['form'] = CustomAuthenticationForm()
    return render(request, template_name=template_name, context=context)



def signout(request):
    logout(request=request)
    return redirect(to='/')


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            # login user
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('/')
        else:
            template_name = 'accounts/signup.html'
            context = {'form': CustomUserCreationForm()}
            return render(request, template_name=template_name, context=context)
    else:
        template_name = 'accounts/signup.html'
        context = {'form': CustomUserCreationForm()}
    return render(request=request, template_name=template_name, context=context)
