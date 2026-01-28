from django.shortcuts import render
from .models import Image
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from orders.models import Order
from .models import Image

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from orders.models import Order
from mediafiles.models import Image
from django.contrib.contenttypes.models import ContentType

@login_required
def downloads_view(request):
    """
    نمایش تمام فایل‌ها / تصاویر مرتبط با محصولاتی که کاربر خریداری کرده
    """
    # گرفتن سفارش‌های پرداخت شده کاربر
    paid_orders = Order.objects.filter(buyer=request.user, paid=True).select_related("product")

    files = Image.objects.none()
    if paid_orders.exists():
        # گرفتن ContentType مدل Product
        product_ct = ContentType.objects.get_for_model(paid_orders.first().product.__class__)
        product_ids = [order.product.id for order in paid_orders]

        # گرفتن تصاویر مربوط به محصولات خریداری شده
        files = Image.objects.filter(content_type=product_ct, object_id__in=product_ids)

    return render(request, "mediafiles/downloads.html", {
        "orders": paid_orders,
        "files": files,
    })

def gallery_view(request):
    files = Image.objects.all()
    return render(request, "mediafiles/list.html", {"files": files})
