from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image
from django.contrib.auth.models import User

COLLEGE_CHOICES = (
    ('Vellore Institute of Technology, Bhopal',
     'Vellore Institute of Technology, Bhopal'),
    ('Vellore Institute of Technology, Vellore',
     'Vellore Institute of Technology, Vellore'),
    ('Vellore Institute of Technology, Chennai',
     'Vellore Institute of Technology, Chennai'),
    ('Vellore Institute of Technology, Amravati',
     'Vellore Institute of Technology, Amravati'),
)


class User(AbstractUser):
    #    is_alumni = models.BooleanField(default=False)
    is_college = models.BooleanField(default=False)
    College = models.CharField(
        max_length=80,
        choices=COLLEGE_CHOICES,
        default="None"
    )
    About = models.TextField(max_length=800)
    Work = models.TextField(max_length=50)
    Year_Joined = models.CharField(max_length=4)
    Branch = models.CharField(max_length=50)
    Image = models.ImageField(
        upload_to='images',
        default='default/test.png'
    )
    Verified = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.Image.path)
        if img.height > 500 or img.width > 500:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.Image.path)
