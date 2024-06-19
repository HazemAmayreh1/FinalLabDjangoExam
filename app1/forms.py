from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'age', 'gender']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter the Student Name', 'class': 'form-control custom-input'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter the Student Email', 'class': 'form-control custom-input'}),
            'age': forms.NumberInput(attrs={'placeholder': 'Enter the Student Age', 'class': 'form-control custom-input'}),
            'gender': forms.Select(attrs={'placeholder': 'Select Gender', 'class': 'form-control custom-input'})
        }
