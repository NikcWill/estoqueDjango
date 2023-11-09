from django.db import models

class User(models.Model):

    name = models.CharField(max_length=100)
    usuario = models.CharField(max_length=100)
    email = models.EmailField()
    senha = models.CharField(max_length=100)
    cod = models.IntegerField()
    in_stock = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
