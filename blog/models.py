from django.conf import settings
from django.db import models
from django.utils import timezone


class Person(models.Model):
    person_id = models.Index
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    #city = models.
    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)
# Create your models here.

class Comin(models.Model):
    comin_id = models.Index
    person_id = models.ForeignKey('Person', on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now=False, auto_now_add=False)
    
    def __str__(self):
        return "%s" % self.data

class Comout(models.Model):
    comout_id = models.Index
    person_id = models.ForeignKey('Person', on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now=False, auto_now_add=False)
    
    def __str__(self):
        return "%s" % self.data

class Department(models.Model):
    department_id = models.Index
    person_id = models.ForeignKey('Person', on_delete=models.CASCADE)
    city = models.CharField(max_length=20)
    name = models.CharField(max_length=20)

    def __str__(self):
        return "%s %s" % (self.name, self.city)

