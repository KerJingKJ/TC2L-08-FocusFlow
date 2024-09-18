from django.db import models
from django.contrib.auth.models import User #to be use later to deal with user log in and log out 
from django.conf import settings

# Create your models here.

class ToDoList(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=300)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title

    def progress(self):
        if self.completed:
            return "Completed."
        else:
            return "Not complete."



# Notes:
# CharField is to use to store a string, and here i set the length of string to be 300 at most.
# TextField can store more string than CharField, use for user to type in the description.
# default for description is True because it allows user to also save their goals even they didn't type in description
# default for completed is False = the first time user create goals, it is incomplete for default