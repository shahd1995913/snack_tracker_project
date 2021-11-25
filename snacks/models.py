from django.db import models

# Create your models here.

from django.contrib.auth import get_user_model


class Snack(models.Model):


    description = models.TextField()

    name = models.CharField(max_length=64)

    purchaser = models.ForeignKey (get_user_model(), on_delete = models.CASCADE, default=1)




    def __str__(self) :

        return self.name