from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Question(models.Model):
      question_text=models.CharField(max_length=1000)
      pub_date=models.DateTimeField('date publidhed')
      def __str__(self):
            return self.question_text
      def was_published_recently(self):
            return self.pub_date>=timezone.now()
class Choice(models.Model):
      question=models.ForeignKey(Question,on_delete=
                                 models.CASCADE)
      choice_text=models.CharField(max_length=500)
      votes=models.IntegerField(default=0)
      def __str__(self):
            return self.choice_text
datetime.timedelta(days=1)
