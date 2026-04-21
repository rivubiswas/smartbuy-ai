from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product
from .models import Cart, CartItem
from recommendations.models import UserActivity
from django.contrib.auth.decorators import login_required


@login_required
def cart_view(request):
    user = request.user
    cart_items = Cart.objects.filter(user=user)
    return render(request, 'cart/cart.html', {'cart_items': cart_items})

def add_to_cart(request, product_id):

    product = get_object_or_404(Product, id=product_id)

    cart, created = Cart.objects.get_or_create(user=request.user)

    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

    if not created:
        cart_item.quantity += 1
        cart_item.save()

        if request.user.is_authenticated:
            UserActivity.objects.create(
            user=request.user,
            product=product,
            action="cart"
    )

    return redirect("/cart/")


def cart_view(request):

    cart = Cart.objects.filter(user=request.user).first()

    items = []

    total = 0

    if cart:
        items = CartItem.objects.filter(cart=cart)

        for item in items:
            total += item.total_price()

    return render(request, "cart.html", {"items": items, "total": total})


def remove_from_cart(request, item_id):

    item = get_object_or_404(CartItem, id=item_id)

    item.delete()

    return redirect("/cart/")