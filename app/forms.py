from django import forms
from app.models import *
class TopicForm(forms.ModelForm):
    class Meta():
        model=Topic
        fields='__all__'

class WebpageForm(forms.ModelForm):
    class Meta():
        model=Webpage
        fields='__all__'
        #fields=['topic_name','name','url']
        #labels={'topic_name':'TN'}
        #exclude=['url']
        #widgets={'url':forms.PasswordInput}


class AccessRecordForm(forms.ModelForm):
    class Meta():
        model=AccessRecord
        fields='__all__'