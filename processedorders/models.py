from django.db import models


class ProcessedOrder(models.Model):
    orderId = models.CharField(
        max_length=10, primary_key=True)
    orderDate = models.CharField(max_length=100)
    customerId = models.CharField(max_length=255)
    units = models.CharField(max_length=15)
    amount = models.CharField(max_length=15)
    remarks = models.CharField(max_length=1000)
    status= models.CharField(max_length=1000)