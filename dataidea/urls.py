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
    path(route='users/', view=include('accounts.urls'), name='accounts'),
    path(route='accounts/', view=include('allauth.urls')),
    path(route='tools/', view=include('tools.urls'), name='tools'),
    # 0auth routes
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)