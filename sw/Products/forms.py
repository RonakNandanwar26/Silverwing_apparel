from django import forms
from .models import Product,Category,Ratings

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','description','category','gender','price','quantity','availability','featured','image1','image2','image3','image4','video1']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),

        }


class Category_Form(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"
        widgets = {
            "name" : forms.TextInput(attrs={'class':'form-control'})
        }


class Rating_Form(forms.ModelForm):
    class Meta:
        model = Ratings
        fields = ['subject','comment','rate']