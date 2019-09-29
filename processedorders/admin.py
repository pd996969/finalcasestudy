from django.contrib import admin
from processedorders.models import ProcessedOrder


class ProcessedOrderAdmin(admin.ModelAdmin):
    list_display = [
            'orderId', 'orderDate',
            'customerId', 'units', 'amount', 'remarks','status'
        ]


admin.site.register(ProcessedOrder, ProcessedOrderAdmin)
