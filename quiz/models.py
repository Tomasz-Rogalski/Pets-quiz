from django.db import models

class Category(models.Model):
    """Category type of questions"""
    name = models.CharField(max_length = 24)

    def __str__(self):
        return self.name
