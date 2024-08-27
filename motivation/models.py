from django.db import models

# Create your models here.
class Actor(models.Model):
    quoter = models.CharField(max_length=225)

    def __str__(self):
        return self.quoter

class Quote(models.Model):   # going to pass quote 
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE) # way of linking two models together, anytime an actor is deleted every single quoted is creator on actor will be deleted 
    quote = models.CharField(max_length=225)

    def __str__(self):
        return str(self.actor) 