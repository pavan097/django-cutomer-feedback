from django.conf.urls import url
from orders.views import *

urlpatterns = [
    url(r'request_order/', returnOrders),
]