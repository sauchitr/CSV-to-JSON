from django import forms
from .models import CSVFile

# Creating form to accept the file using FileField and 
# integer using the IntegerField.

class CSVFileForm(forms.ModelForm):
    csv_file = forms.FileField(label='Upload CSV file')
    time_frame = forms.IntegerField(label='Enter time frame')

    # using class meta to overwrite the CSVFile Model
    class Meta:
        model = CSVFile
        fields = ["id", "csv_file"]

