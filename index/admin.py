from .models import Price
from .models import Service
from .models import Feature
from .models import Contact
from .models import Feedback
from .models import Partner
from .models import Portfolio
from .models import Testimonial
from .models import CompanyInfo
from django.contrib import admin
from .models import TermOfService
from .models import PrivacyPolicy
from .models import FrequentlyAskedQuestion

# Admin Models
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject']
    list_filter = ['name', 'email']
    search_fields = ['name', 'email', 'subject']

# Register your models here.
admin.site.register(model_or_iterable=Feedback, admin_class=FeedbackAdmin)
admin.site.register(model_or_iterable=
                    [Partner, PrivacyPolicy, TermOfService, Service, Feature, Testimonial, Portfolio, CompanyInfo, Price, FrequentlyAskedQuestion, Contact])




