from django.db import models
from django.contrib.auth.models import User 

class Task(models.Model):
    title= models.CharField(max_length=30)
    isItDone= models.BooleanField(default=False)
    date_time= models.DateTimeField(auto_now_add=True)
    user= models.ForeignKey(User, on_delete=models.CASCADE, default= None)

    def __str__(self):
        return self.title

