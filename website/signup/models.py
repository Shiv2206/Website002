from django.db import models

# Create your models here.
class signup(models.Model):
    First_name=models.CharField(max_length=100)
    Last_name=models.CharField(max_length=100)
    User_name=models.CharField(max_length=100)
    Email=models.EmailField(max_length=100)
    Password=models.CharField(max_length=100)
    C_Pass=models.CharField(max_length=100)
    def __str__(self):
        return self.First_name
    