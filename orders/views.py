from django.shortcuts import render, redirect
from cart.models import Cart, CartItem
from .models import Order, OrderItem
from recommendations.models import UserActivity


# CHECKOUT VIEW
def checkout(request):

    cart = Cart.objects.filter(user=request.user).first()

    if not cart:
        return redirect("/")

    items = CartItem.objects.filter(cart=cart)

    total = 0

    for item in items:
        total += item.total_price()

    if request.method == "POST":

        # 🔥 Create Order
        order = Order.objects.create(
            user=request.user,
            total_price=total
        )

        # 🔥 Create Order Items + Track Purchase
        for item in items:

            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price
            )

            # 🔥 IMPORTANT: Track purchase for recommendation system
            if request.user.is_authenticated:
                UserActivity.objects.create(
                    user=request.user,
                    product=item.product,
                    action="purchase"
                )

        # 🔥 Clear cart after order
        items.delete()

        return redirect("/orders/")

    return render(request, "checkout.html", {
        "items": items,
        "total": total
    })


# ORDER HISTORY VIEW
def order_history(request):

    orders = Order.objects.filter(user=request.user).order_by('-created_at')

    return render(request, "orders.html", {
        "orders": orders
    })