from django.db import models

class product(models.Model):
    product_ID=models.AutoField
    product_Name=models.CharField(max_length=100)
    product_Price=models.IntegerField()
    product_Description=models.TextField()
    
    
    def __str__(self):
        return self.product_Name
    
# Create your models here.
