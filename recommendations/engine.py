from .models import UserActivity
from products.models import Product
from collections import Counter
import random


def get_recommended_products(user):

    activities = UserActivity.objects.filter(user=user)

    # ❌ If no activity → show random products
    if not activities.exists():
        return Product.objects.order_by('?')[:6]

    category_scores = Counter()
    product_scores = Counter()

    # 🔥 Build scores
    for activity in activities:

        # category weight
        category_scores[activity.product.category] += 2

        # product weight (for repeat interest)
        product_scores[activity.product.id] += 3

    # 🔥 Get top category
    top_categories = [cat for cat, _ in category_scores.most_common(2)]

    # 🔥 Fetch products from those categories
    recommended = Product.objects.filter(category__in=top_categories)

    # ❌ Remove already viewed products
    viewed_ids = [a.product.id for a in activities]
    recommended = recommended.exclude(id__in=viewed_ids)

    # 🔥 Shuffle for randomness
    recommended = list(recommended)
    random.shuffle(recommended)

    return recommended[:6]