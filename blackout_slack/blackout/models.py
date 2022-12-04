from django.db import models

# Create your models here.
class LastCheck(models.Model):
    user = models.CharField(max_length=20)
    date = models.DateTimeField()
    token = models.CharField(max_length=200)
    headers = models.JSONField()
    def __str__(self):
        return "%s %r"(self.user, self.date)
