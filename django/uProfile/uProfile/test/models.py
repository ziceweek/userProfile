from django.db import models


class t1(models.Model):
    uid = models.IntegerField(max_length=11)
    name = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name