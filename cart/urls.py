from django.urls import path
from .views import add_to_cart, cart_view, remove_from_cart


urlpatterns = [

    path("add-to-cart/<int:product_id>/", add_to_cart),

    path("cart/", cart_view),

    path("remove/<int:item_id>/", remove_from_cart),

]