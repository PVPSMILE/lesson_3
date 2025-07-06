from django.db import models

# Create your models here.
class NavBar(models.Model):
    name = models.CharField(max_length=100)
    url = models.TextField()
    
    def __str__(self):
        return self.name




