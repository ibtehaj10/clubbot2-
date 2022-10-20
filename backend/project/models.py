# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Club(models.Model):
    id = models.IntegerField(primary_key=True)
    number = models.CharField(max_length=13)
    name = models.CharField(max_length=100)
    seat = models.IntegerField()
    song = models.CharField(max_length=100)
    time = models.DateTimeField()
    status = models.IntegerField()
    ques1 = models.IntegerField()
    ques2 = models.IntegerField()
    alldone = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'club'



