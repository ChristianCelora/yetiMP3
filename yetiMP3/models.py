from django.db import models

class Task(models.Model):
    id = models.AutoField(primary_key=True)
    status = models.BooleanField(default=False)
    file_name = models.CharField(max_length=255, null=True)
    frontend_name = models.CharField(max_length=255, default="")
