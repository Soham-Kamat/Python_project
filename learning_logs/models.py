from django.db import models # Model tells how to work with the data stored in the app.
from django.contrib.auth.models import User

# Create your models here.  
class Topic(models.Model):
    "A topic that user is learning about."
    text=models.CharField(max_length=200)
    date_added=models.DateTimeField(auto_now_add=True)
    owner=models.ForeignKey(User,on_delete=models.CASCADE)


    def __str__(self):  #Method returns string representation of object
        return self.text

class Entry(models.Model):
    topic=models.ForeignKey(Topic,on_delete=models.CASCADE)
    text=models.TextField()
    date_added=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural="entries"

    def __str__(self):
        "Return a string representation of a model"
        return f"{self.text[:50]}..." 
