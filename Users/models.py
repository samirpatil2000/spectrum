from django.db import models
from django.contrib.auth.models import User

from cropperjs.models import CropperImageField

# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    #profile_pic=CropperImageField(upload_to='profile_pics')
    profile_pic=models.ImageField(upload_to='profile_pics')
    bio= models.TextField(default='Add Your Bio Here')
    phone_number=models.IntegerField(max_length=10,default=0)


    def __str__(self):
        return f'{self.user.username} Profile'