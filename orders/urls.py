from django.urls import path
from .views import checkout, order_history


urlpatterns = [

    path("checkout/", checkout),

    path("orders/", order_history),

]