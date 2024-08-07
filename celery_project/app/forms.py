from django.forms import ModelForm
from .models import *



class itemform(ModelForm):
    class Meta:
        model =item
        fields={'content','user',}