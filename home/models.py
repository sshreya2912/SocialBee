from django.db import models

# Create your models here.
class Contact(models.Model):
    sr_no=models.AutoField(primary_key=True)
    name=models.CharField(max_length=40)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=13)
    subject=models.TextField(max_length=100)
    def __str__(self):
        return self.name


