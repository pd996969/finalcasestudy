from django.conf.urls import url
from processedorders.views import ProcessedOrdersView

urlpatterns = [
    url(r'processedorders', ProcessedOrdersView.as_view(), name='processedorders_all'),
    url(r'user8lambda', ProcessedOrdersView.as_view(), name='customer_info')
]