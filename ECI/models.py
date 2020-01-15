from django.db import models

# Create your models here.

class Gallery(models.Model):
    name=models.CharField(max_length=250)
    image=models.ImageField(upload_to='gallery')
    desc=models.TextField()
    def __str__(self):
        return self.name

class Details(models.Model):
    name=models.CharField(max_length=250)
    email=models.CharField(max_length=250)
    username=models.CharField(max_length=250)
    password=models.CharField(max_length=250)
    eci_id=models.CharField(max_length=250)
    gender=models.CharField(max_length=250)
    address=models.CharField(max_length=1000)
    prior_experience=models.IntegerField()

    def __str__(self):
        return self.eci_id + ' - '+ self.name    

class Progress(models.Model):
    #id_details=models.ForeignKey(Details,on_delete=models.CASCADE)
    email=models.CharField(max_length=250)
    level=models.IntegerField()
    no_of_events_conducted=models.IntegerField()
    rating=models.IntegerField()
    digital_badge=models.IntegerField()
    score=models.IntegerField()

    def __int__(self):
        return self.score 

class Images(models.Model):
    id_details=models.ForeignKey(Details,on_delete=models.CASCADE)
    name=models.CharField(max_length=250)
    desc=models.TextField()
    pic=models.ImageField(upload_to='pics')
    completion_status=models.BooleanField(default=False)
    url_link=models.URLField()
    def __str__(self):
        return self.name 

           
     