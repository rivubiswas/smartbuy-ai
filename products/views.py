from django.shortcuts import render, get_object_or_404
from .models import Product
from recommendations.models import UserActivity


def home(request):

    products = Product.objects.all()

    return render(request,"home.html",{"products":products})


def product_detail(request,id):

    product = get_object_or_404(Product,id=id)

    return render(request,"product_detail.html",{"product":product})

from reviews.models import Review


def product_detail(request,id):

    product = Product.objects.get(id=id)

    reviews = Review.objects.filter(product=product, is_fake=False)

    return render(request,"product_detail.html",{
        "product":product,
        "reviews":reviews
    })




def product_detail(request,id):

    product = Product.objects.get(id=id)

    # Track user activity
    if request.user.is_authenticated:
        UserActivity.objects.create(
            user=request.user,
            product=product,
            action="view"
        )

    from reviews.models import Review
    reviews = Review.objects.filter(product=product, is_fake=False)

    return render(request,"product_detail.html",{
        "product":product,
        "reviews":reviews
    })
    
from recommendations.engine import get_recommended_products


def home(request):

    products = Product.objects.all()

    recommended = []

    if request.user.is_authenticated:
        recommended = get_recommended_products(request.user)

    return render(request,"home.html",{
        "products":products,
        "recommended":recommended
    })