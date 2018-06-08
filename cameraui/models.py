# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Cam12presets(models.Model):
    start_x = models.FloatField()
    start_y = models.FloatField()
    start_z = models.FloatField()
    title = models.CharField(max_length = 100)
    def __str__(self):
        return self.title

class Cam12pr(models.Model):
    start_x = models.FloatField()
    start_y = models.FloatField()
    start_z = models.FloatField()
    title = models.CharField(max_length = 100)
    def __str__(self):
        return self.title
# Create your models here.
