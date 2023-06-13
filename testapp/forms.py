from django import forms
from django.core import validators

class FeedBackForm(forms.Form):
    name=forms.CharField()
    rollno=forms.IntegerField()
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput)
    rpassword=forms.CharField(widget=forms.PasswordInput)
    feedback=forms.CharField(widget=forms.Textarea)


def clean(self):
    print('Total Form Validation....')
    cleaned_data = super().clean()
    inputpwd=cleaned_data['password']
    inputrpwd=cleaned_data['rpassword']
    if inputpwd != inputrpwd:
        raise forms.ValidationError('password not matched')