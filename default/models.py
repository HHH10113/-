from django.db import models

# Create your models here.
class Poll(models.Model):
    suject = models.CharField(max_length=225)
    description = models.TextField()
    data_created = models.DateField(auto_now_add = True)

    def __str__(self):
        return str(self.id)+")"+self.suject
    #opt1 = models.CharField(max_length=225)
    #opt2 = models.CharField(max_length=225)
    #opt3 = models.CharField(max_length=225)
    #opt4 = models.CharField(max_length=225)

class Option(models.Model):
    poll_id = models.IntegerField()
    title = models.CharField(max_length=225)
    count = models.IntegerField(default=0)