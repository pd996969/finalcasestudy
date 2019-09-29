from rest_framework import serializers
from processedorders.models import ProcessedOrder


class ProcessedOrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProcessedOrder
        fields = [
            'orderId', 'orderDate',
            'customerId', 'units', 'amount', 'remarks','status'
        ]