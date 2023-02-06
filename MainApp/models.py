from django.db import models


# Creating a model to save the uploaded csv file

class CSVFile(models.Model):
    csv_file = models.FileField(upload_to='csv/')
