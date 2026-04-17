from django.contrib import admin
from django.urls import path, include
from products.views import home

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path('admin/', admin.site.urls),

    path('', home),

    path('', include('accounts.urls')),

    path('', include('products.urls')),

    path('', include('cart.urls')),
    
    path('', include('orders.urls')),
    
    path('', include('reviews.urls')),
    
    path('', include('chatbot.urls')),
]

# 🔥 THIS LINE FIXES YOUR IMAGE ISSUE
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)