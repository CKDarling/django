from django import forms
from django.core import validators
# Example of how you would create your own validators
#def check_for_z(value):
    #if value[0].lower() != 'z':
    #    raise forms.ValidationError("NAME NEEDS TO START WITH Z")
    #    add (validators=[check_for_z]) to your desired field
    # here we would have added it to name

class FormX(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Verify Email:')
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False,
                               widget=forms.HiddenInput,
                               validators=[validators.MaxLengthValidator(0)])
# bot catcher prevents webscraping

# cleans all data at once
    def clean(self):
        all_clean_data=super().clean()
        email=all_clean_data['email']
        vmail=all_clean_data['verify_email']

        if email!=vmail:
            raise forms.ValidationError("Make sure the emails match!")
