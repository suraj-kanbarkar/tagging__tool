from django.db import models


# Create your models here.

class TagData(models.Model):
    objects = models.Manager()
    text = models.TextField(default=None, null=True, blank=True)
    oc = models.CharField(max_length=50, default=None, blank=True, null=True)
    noc = models.CharField(max_length=50, default=None, blank=True, null=True)
    subject = models.CharField(max_length=100, default=None, blank=True, null=True)
    attribute = models.CharField(max_length=200, default=None, blank=True, null=True)
    status = models.CharField(max_length=20, default=None, blank=True, null=True)

    def __str__(self):
        template = '{0.text} {0.oc} {0.noc} {0.subject} {0.attribute} {0.status}'
        return template.format(self)
