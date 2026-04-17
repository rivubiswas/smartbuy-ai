from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings
from products.models import Product


class UserActivity(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    action = models.CharField(max_length=50)  # view, purchase

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.product} - {self.action}"