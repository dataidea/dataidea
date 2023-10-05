from django.shortcuts import render

# Create your views here.
def jumaShafara(request):
    template_name = 'profiles/jumashafara.html'
    return render(request=request, template_name=template_name)