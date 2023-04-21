from django.db import models
from django.contrib.auth import get_user_model
user=get_user_model()

class profile(models.Model):
    fname=models.TextField()
    lname=models.TextField()
    uname=models.TextField()
    email=models.EmailField()
    address=models.TextField()
    pp=models.ImageField(upload_to='proficpic')
    def __str__(self):
        return self.uname+' ('+self.fname+' ' +self.lname+' )'

