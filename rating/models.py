from distutils.command.upload import upload
from email.mime import image
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class RateStars(models.Model):
    image = models.ImageField(upload_to="images/")
    score = models.IntegerField(default=0,
            validators=[
                MaxValueValidator(5),
                MinValueValidator(0)
            ]                    
        )
    
    def __str__(self):
        return f"{str(self.pk)}-chi"