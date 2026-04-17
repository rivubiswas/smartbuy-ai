from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Review
from products.models import Product
from bot_detection.detector import is_fake_review


def add_review(request, product_id):

    product = Product.objects.get(id=product_id)

    if request.method == "POST":

        text = request.POST.get("text")
        rating = request.POST.get("rating")

        fake = is_fake_review(text)

        Review.objects.create(
            user=request.user,
            product=product,
            text=text,
            rating=rating,
            is_fake=fake
        )

        return redirect(f"/product/{product_id}/")

    return redirect("/")