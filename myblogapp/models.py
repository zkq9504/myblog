from django.db import models


class Skill(models.Model):
    type = models.CharField(max_length=10)
    title = models.CharField(max_length=30)
    abstract = models.CharField(max_length=250)
    href = models.URLField()
    time = models.DateTimeField()

    class Meta():
        db_table = "skill"

class Life(models.Model):
    type = models.CharField(max_length=10)
    title = models.CharField(max_length=30)
    abstract = models.CharField(max_length=250)
    href = models.URLField()
    time = models.DateTimeField()

    class Meta():
        db_table = "life"

class Food(models.Model):
    type = models.CharField(max_length=10)
    title = models.CharField(max_length=30)
    abstract = models.CharField(max_length=250)
    href = models.URLField()
    time = models.DateTimeField()

    class Meta():
        db_table = "food"

class Msgboard(models.Model):
    time = models.DateTimeField()
    message = models.CharField(max_length=250)

    class Meta():
        db_table = "msgboard"

class Comments(models.Model):
    time = models.DateTimeField()
    text = models.CharField(max_length=250)

    class Meta():
        db_table = "comments"
