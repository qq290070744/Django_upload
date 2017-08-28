from django.db import models


# Create your models here.

class UploadFile(models.Model):
    userid = models.CharField(max_length=30)
    file = models.FileField(upload_to='./upload/')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        self.userid
