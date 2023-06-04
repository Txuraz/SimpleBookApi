from django.db import models

class ScannedImage(models.Model):
    image = models.ImageField(upload_to='scanned_images/')
