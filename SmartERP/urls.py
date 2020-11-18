from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from SmartERP import api_urls

urlpatterns = [
    path('erp/admin/', admin.site.urls),
    # path('erp/category/', include('category.urls'), name='category'),
    path('erp/company/', include('company.urls'), name='company'),
    path('erp/customer/', include('customer.urls'), name='customer'),
    path('erp/document/', include('document.urls'), name='document'),
    path('erp/user/', include('erp_user.urls'), name='user'),
    path('erp/finance/', include('finance.urls'), name='finance'),
    path('erp/order/', include('order.urls'), name='order'),
    path('erp/price/', include('price.urls'), name='price'),
    path('erp/product/', include('product.urls'), name='product'),
    path('erp/reference/', include('reference.urls'), name='reference'),
    path('erp/unit/', include('unit.urls'), name='unit'),
    path('erp/warehouse/', include('warehouse.urls'), name='warehouse'),
    path('erp/dashboard/', include('dashboard.urls'), name='dashboard'),
    path('', include(api_urls), name='api'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
