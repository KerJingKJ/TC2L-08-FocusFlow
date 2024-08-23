from django.db import models
from django.contrib.auth.models import User #to be use later to deal with user log in and log out 

# Create your models here.

class ToDoList(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    #to be use later when log in log out feature is ready
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title





# Notes:
# CharField is to use to store a string, and here i set the length of string to be 300 at most.
# TextField can store more string than CharField, use for user to type in the description.