from django.db import models


class Profile(models.Model):
    First_name = models.CharField(max_length=100)
    Last_name = models.CharField(max_length=100)
    Email = models.EmailField()
    Username = models.CharField(max_length=50)
    Password = models.CharField(max_length=50)
    Domain = models.CharField(max_length=50)

    def __str__(self):
        return self.Username

