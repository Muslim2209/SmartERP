from django.urls import include, path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny

schema_view = get_schema_view(
    openapi.Info(title="SmartERP",
                 default_version='v1.0.0',
                 description="API for SmartERP",
                 # terms_of_service="https://www.google.com/policies/terms/",
                 # contact=openapi.Contact(email="contact@snippets.local"),
                 # license=openapi.License(name="BSD License")
                 ), public=True, permission_classes=(AllowAny,)
)

urlpatterns = [
    # path('category/', include('category.api.urls'), name='api_category'),
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
    path('wh/', include('warehouse.api.urls'), name='api_warehouse'),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
