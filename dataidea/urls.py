"""
URL configuration for ideamovies project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from django.urls import include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path(route = 'admin/', view=admin.site.urls),
    path(route='', view=include('index.urls'), name='index'),
    path(route='blog/', view=include('blog.urls'), name='blog'),
    path(route='school/', view=include('school.urls'), name='school'),
    path(route='profiles/', view=include('profiles.urls'), name='profiles'),
    path(route='accounts/', view=include('accounts.urls'), name='accounts'),
    path(route='tools/', view=include('tools.urls'), name='tools')
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)