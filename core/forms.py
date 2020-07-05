from django import forms

class ResumeForm(forms.Form):
    docfile = forms.FileField(label='Upload resume....')