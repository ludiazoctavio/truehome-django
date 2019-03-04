from django.db import models

class Property(models.Model):

    owner = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    image = models.ImageField(upload_to='posts/photos')

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):

        return self.owner