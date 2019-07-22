from django.db import models


class Msgboard(models.Model):
    time = models.DateTimeField()
    message = models.CharField(max_length=250)

    class Meta():
        db_table = "msgboard"