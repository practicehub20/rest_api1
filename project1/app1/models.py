from django.db import models

class ProductModel(models.Model):
    idno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)
    price = models.FloatField()
    qty = models.IntegerField()
