from django.db import models

# Theme model

class SiteSettings(models.Model):
    image = models.ImageField(upload_to = 'media/site/')
    caption = models.TextField()
