from django.urls import include, path
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view

urlpatterns = [
    path('category/', include('category.api.urls'), name='api_category'),
    path('company/', include('company.api.urls'), name='api_company'),
    path('customer/', include('customer.api.urls'), name='api_customer'),
    path('dashboard', include('dashboard.api.urls'), name='api_dashboard'),
    path('document/', include('document.api.urls'), name='api_document'),
    path('user/', include('erp_user.api.urls'), name='api_user'),
    path('finance/', include('finance.api.urls'), name='api_finance'),
    path('order/', include('order.api.urls'), name='api_order'),
    path('price/', include('price.api.urls'), name='api_price'),
    path('product/', include('product.api.urls'), name='api_product'),
    path('reference/', include('reference.api.urls'), name='api_reference'),
    path('unit/', include('unit.api.urls'), name='api_unit'),
    path('warehouse/', include('warehouse.api.urls'), name='api_warehouse'),
    path('openapi/', get_schema_view(title="SmartERP", description="API for SmartERP",
                                     version="1.0.0"), name='openapi-schema'),
    path('swagger/', TemplateView.as_view(template_name='swagger/swagger-ui.html',
                                          extra_context={'schema_url': 'openapi-schema'}), name='swagger-ui'),
    path('redoc/', TemplateView.as_view(template_name='swagger/redoc.html',
                                        extra_context={'schema_url': 'openapi-schema'}), name='redoc'),
]
