from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_data = models.DateTimeField("Date Published")

class Choices(models.Model):
    question=models.ForeignKey(Question,on_delete = models.CASCADE)
    choices_text=models.CharField(max_length=200)
    vote= models.IntegerField(default = 0)