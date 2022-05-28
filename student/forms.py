
from django import forms
from student.models import Person

# Creating a form
class MyForm(forms.ModelForm):
    class Meta:
        model = Person

        fields = ["first_name", "last_name"]
        
