from django.db import models


class information(models.Model):
    Name = models.CharField(max_length=250)
    Email = models.CharField(max_length=250)
    Message = models.CharField(max_length=250)

    def __str__(self):
        return self.Name
