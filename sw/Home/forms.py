from .models import *
from django import forms

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"


class UserForm(forms.ModelForm):
    username = forms.CharField(max_length=20, disabled=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ))
    email = forms.EmailField(max_length=50, disabled=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ))
    class Meta:
        model = User
        fields = ['username','email']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name','last_name','bio','tel','gender','age','address','file']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'bio': forms.Textarea(attrs={'class': 'form-control'}),
            'tel': forms.NumberInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'})
        }