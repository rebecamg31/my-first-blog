from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    author= models.ForeignKey('auth.User', on_delete = models.CASCADE) #ForeignKey is a link to another model
    title = models.CharField(max_length = 200) #How to define text with a limited number of characters
    text = models.TextField() #This is for long text without a limit
    created_date = models.DateTimeField( #This is a date and time
        default = timezone.now)
    published_date = models.DateTimeField(
        blank = True, null = True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title




