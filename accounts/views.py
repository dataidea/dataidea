from django.db.models import Q
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth import logout
# from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.


def signin(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
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
            context = {'form': AuthenticationForm(), 'error': error}
            return render(request, template_name=template_name, context=context)
    else:
        template_name = 'accounts/signin.html'
        context = {'form': AuthenticationForm()}
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
            # Customize error messages
            error = form.errors
            template_name = 'accounts/signup.html'
            context = {'form': CustomUserCreationForm(), 'error': error}
            return render(request, template_name=template_name, context=context)
    else:
        template_name = 'accounts/signup.html'
        context = {'form': CustomUserCreationForm()}
    return render(request=request, template_name=template_name, context=context)
