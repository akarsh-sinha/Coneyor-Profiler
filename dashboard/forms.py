from django import forms
from .models import DataFile

class DataFileForm(forms.ModelForm):
    class Meta:
        model = DataFile
        fields = ['date', 'file1', 'file2']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'file1': 'Left Profile',
            'file2': 'Right Profile',
        }

class DateForm(forms.Form):
    date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
