from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('i18n/', include('django.conf.urls.i18n')),
    path('', include("core.urls")),
    path('accounts/', include("accounts.urls")),
    path('products/', include("products.urls")),
    path('orders/', include("orders.urls")),
    path('mediafiles/', include("mediafiles.urls")),
    path('contact/', include("contact.urls")),
]

# سرو کردن فایل‌های media و (در صورت نیاز) static در حالت توسعه
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) if hasattr(settings, "STATIC_ROOT") else []
