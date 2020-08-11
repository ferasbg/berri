from .models import (
    User, Modules)
#we can calculate session_time per question by comparing the total time elapsed between the starttime and the instance for each user_ answer_choice
# .objects.get() for retrieving stored db objects


# define multiple choice field in which its response will hit the db to pull a value, and if the value does not match the value selected from the multiple choice, then the user_answer_choice is WRONG
class ModulesForm(forms.ModelForm)
    choice_field = forms.MultipleChoiceField(choices=choices, widget=forms.CheckboxSelectMultiple)

