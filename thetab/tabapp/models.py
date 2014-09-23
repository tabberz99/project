from django.db import models

# Create your models here.
class Variables(models.Model):
    title = models.CharField(max_length=50)
    maxMarks = models.IntegerField()
    minMarks = models.IntegerField()
    
    def __unicode__(self):
      return self.title
    
#class ScoreForm(models.Model):
    #formname = models.CharField(max_length=50)
    #components = models.ManyToManyField(Variable)
    
    #def __unicode__(self):
      #return self.formname