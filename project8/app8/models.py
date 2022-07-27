from django.db import models

# Create your models here.

class Register(models.Model):
    first_name=models.CharField(max_length=264,unique=True)
    last_name=models.CharField(max_length=264,unique=True)
    email_id=models.CharField(max_length=264,unique=True)
    user_name=models.CharField(max_length=264,unique=True)
    password=models.CharField(max_length=264,unique=True)
    conform_password=models.CharField(max_length=264,unique=True)

    def __str__(self):
        return self.first_name

    