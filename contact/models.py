from django.db import models

# Create your models here.


class User(models.Model):
    user_id = models.IntegerField(default=0)
    user_name = models.CharField(max_length=100)
    email_address = models.EmailField()
    address = models.TextField()
    query = models.TextField(null=True)
