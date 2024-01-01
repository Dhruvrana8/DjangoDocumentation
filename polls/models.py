import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("Date Published")
    
    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choices(models.Model):
    question=models.ForeignKey(Question,on_delete = models.CASCADE)
    choices_text=models.CharField(max_length=200)
    vote= models.IntegerField(default = 0)
    def __str__(self):
        return self.question_text
    