from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.


class Bu1(models.Model):
    title = models.CharField(max_length=100)
    q1 = models.IntegerField(validators=[MaxValueValidator(5)])
    q2 = models.IntegerField()
    q3 = models.IntegerField()
    q4 = models.IntegerField()
    q5 = models.IntegerField()

    def __str__(self):
        return self.title