import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Query(models.Model):
    query_text = models.CharField(max_length = 10)
    pub_date = models.DateTimeField('date created')

    def __str__(self):
        return self.query_text

class Text(models.Model):
    query = models.ForeignKey(Query, on_delete=models.CASCADE)
    generated_text = models.CharField(max_length = 300)
    pub_date = models.DateTimeField('date created')

    def __str__(self):
        return '%s : %s' % (self.query, self.generated_text)

    def was_generated_recently(self):
        return timezone.now() - datetime.timedelta(days=1) <= self.pub_date <= timezone.now()
