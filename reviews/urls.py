from django.urls import path
from .views import add_review


urlpatterns = [

    path("add-review/<int:product_id>/", add_review),

]