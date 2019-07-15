from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Myuser(User):
    telephone=models.CharField(max_length=11)