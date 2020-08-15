from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    link = models.CharField(max_length=500)
    desc = models.CharField(max_length=1000)


class View(models.Model):
	intpro = models.IntegerField()
	diginfo = models.IntegerField()
	compandint = models.IntegerField()
