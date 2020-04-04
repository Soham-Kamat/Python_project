from django import forms

from .models import Topic,Entry

class TopicForm(forms.ModelForm):
    class Meta:  #Meta class tells Django which model and  fields to include in the form. 
        model=Topic
        fields=['text']
        labels={'text': ''}

class EntryForm(forms.ModelForm):
    class Meta:
        model=Entry
        fields=['text']
        labels={'text': 'Entry:'}
        widgets={'text':forms.Textarea(attrs={'cols':80})} # attribute to include text-box.




