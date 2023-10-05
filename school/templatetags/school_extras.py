# Create a custom template filter in your Django app
# myapp/templatetags/myapp_extras.py

from django import template # Replace 'myapp' with the actual name of your app

register = template.Library()

@register.filter(name='dict_lookup')
def dict_lookup(dictionary, index):
    try:
        return dictionary[str(index)]
    except (KeyError, ValueError):
        return None

# In your template, load the custom filter at the top of the file

