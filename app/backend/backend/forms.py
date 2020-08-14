from django import forms
from backend import views

class Question(forms.Form):
    options = {
        'a',
        'b',
        'c',
        'd'
    }
    name = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=options)

