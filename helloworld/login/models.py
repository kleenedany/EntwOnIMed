from django.db import models

class User(models.Model):
    user_name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    
    def __str__(self):
        return self.user_name
 
