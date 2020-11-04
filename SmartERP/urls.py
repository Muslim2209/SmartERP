from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.http import HttpResponse
from django.template import loader
from django.urls import include, path, re_path

from SmartERP import api_urls


def index(request):
    context = {}
    template = loader.get_template('app/index.html')
    return HttpResponse(template.render(context, request))


def gentella_html(request):
    context = {}
    # The template to be loaded as per gentelella.
    # All resource paths for gentelella end in .html.

    # Pick out the html file name from the url. And load that template.
    load_template = request.path.split('/')[-1]
    template = loader.get_template('app/' + load_template)
    return HttpResponse(template.render(context, request))


urlpatterns = [
    path('erp/admin/', admin.site.urls),
    path('erp/category/', include('category.urls'), name='category'),
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
    re_path(r'^.*\.html', gentella_html, name='gentella'),
    path('', index, name='index'),
    path('', include(api_urls), name='api'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
