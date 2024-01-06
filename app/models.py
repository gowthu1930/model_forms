from django.db import models

# Create your models here.
class Topic(models.Model):
    topic_name=models.CharField(max_length=20,primary_key=True)
    def __str__(self):
        return self.topic_name
class webpage(models.Model):
    topic_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    url=models.URLField()
    name=models.CharField(max_length=100)
    email=models.EmailField(default='xyz@gmail.com')

    def __str__(self):
        return self.name



class accessrecord(models.Model):
    name=models.ForeignKey(webpage,on_delete=models.CASCADE)
    date=models.DateField()
    author=models.CharField(max_length=200)

    def __str__(self):
        return self.author
