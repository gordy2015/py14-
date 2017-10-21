from django.db import models

# Create your models here.


class UserType(models.Model):
    caption = models.CharField(max_length=32)


class UserGroup(models.Model):
    name = models.CharField(max_length=32)


class UserInfo(models.Model):
    username = models.CharField(max_length=32)
    email = models.EmailField()
    user_type = models.ForeignKey(to='UserType',to_field='id')
    u2g = models.ManyToManyField(UserGroup)

