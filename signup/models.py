from django.db import models
from django.urls import reverse


# Create your models here.


class User(models.Model):
    First_Name = models.CharField(max_length=200, blank=False)
    Last_Name = models.CharField(max_length=200, blank=False)
    DOB = models.CharField(max_length=200, blank=False)
    Loc = models.CharField(max_length=200, blank=False)
    Email = models.CharField(max_length=250, blank=False)
    Password = models.CharField(max_length=250, blank=False)
    Gender = models.CharField(max_length=250, blank=False)
    profile_picture = models.CharField(max_length=250, default='')
    active = models.IntegerField(default=1)

    def get_absolute_url(self):
        return reverse('myprofile:myprofile', kwargs={'pk': self.pk})


class Friends(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    friend_id = models.IntegerField(default=1)
    flag = models.IntegerField(default=1)
