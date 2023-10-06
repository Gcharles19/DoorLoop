from django import forms

class EstateForm(forms.Form):
    Name = forms.CharField(max_length=10)
    Address = forms.CharField(max_length=10)
    Contact = forms.CharField(max_length=10)
    StatusID = forms.IntegerField