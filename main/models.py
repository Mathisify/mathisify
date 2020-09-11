from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    link = models.CharField(max_length=500)
    desc = models.CharField(max_length=1000)


class View(models.Model):
	intpro = models.CharField(max_length=1000)
	diginfo = models.CharField(max_length=1000)
	compandint = models.CharField(max_length=1000)
	histcomp = models.CharField(max_length=1000)
	welcometoscratch = models.CharField(max_length=1000)
	firstprogram = models.CharField(max_length=1000)
