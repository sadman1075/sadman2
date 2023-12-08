from django.db import models
class sadman(models.Model):
      username=models.CharField(max_length=100)
      city=models.CharField(max_length=100)
      thana=models.CharField(max_length=100)
      area=models.CharField(max_length=100)
      type=models.CharField(max_length=100)
      images=models.ImageField(null=True,blank=True,upload_to='sadman')