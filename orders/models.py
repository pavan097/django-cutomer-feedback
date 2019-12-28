from django.db import models

# Create your models here.


class ReturnOrder(models.Model):
    product_id = models.CharField(max_length=50)
    product_type = models.CharField(max_length=50)
    user_email = models.EmailField(max_length=250)
    phone_no = models.CharField(max_length=10)
    description = models.TextField()