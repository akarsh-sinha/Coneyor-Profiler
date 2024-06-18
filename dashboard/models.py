from django.db import models

class DataFile(models.Model):
    date = models.DateField(unique=True)
    file1 = models.FileField(upload_to='data_files/')
    file2 = models.FileField(upload_to='data_files/')

    def __str__(self):
        return str(self.date)
