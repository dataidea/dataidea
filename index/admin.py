from .models import Feedback
from django.contrib import admin
from .models import TermOfService
from .models import PrivacyPolicy

# Admin Models
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject']
    list_filter = ['name', 'email']
    search_fields = ['name', 'email', 'subject']

# Register your models here.
admin.site.register(model_or_iterable=Feedback, admin_class=FeedbackAdmin)
admin.site.register(model_or_iterable=[PrivacyPolicy, TermOfService])




