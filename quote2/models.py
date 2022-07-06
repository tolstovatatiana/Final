from django.db import models

# Create your models

class Quote(models.Model):
    text = models.TextField()
    quote_author = models.TextField()
