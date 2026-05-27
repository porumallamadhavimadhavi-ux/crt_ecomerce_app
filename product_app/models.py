from django.db import models

# Create your models here.
class ProductModel(models.Model):
    id=models.AutoField(primary_key=True)
    p_name=models.CharField(max_length=255)
    p_type=models.CharField(max_length=255)
    p_price=models.FloatField(max_length=255)
    p_quantity=models.CharField(max_length=255)



class Cart(models.Model):
    cart_id=models.AutoField(primary_key=True)
    product_id=models.IntegerField()
    p_price = models.FloatField()