from django.db import models


class Category(models.Model):
    cid = models.AutoField(primary_key=True)
    cname = models.CharField(max_length=50)

    def __str__(self):
        return self.cname
