from django.db import models

# Create your models here.
class Membership(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    plan = models.CharField(max_length=50)
    date_created = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class AI_bot(models.Model):
    username = models.CharField(max_length=120)
    question = models.TextField()
    answer = models.TextField()

    def __self__(self):
        return self.name    