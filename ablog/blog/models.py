from django.db import models

class Form (models.Model):
    title = models.TextField(max_length=120)
    text = models.TextField(max_length=255)