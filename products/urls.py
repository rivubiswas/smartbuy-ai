from django.urls import path
from .views import product_detail


urlpatterns = [

    path("product/<int:id>/", product_detail),

]