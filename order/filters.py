import django_filters

from order.models import Order


class OrderFilter(django_filters.FilterSet):
    start_date = django_filters.DateFilter(field_name='created_date', lookup_expr='gte')
    end_date = django_filters.DateFilter(field_name='created_date', lookup_expr='lte')
    note = django_filters.CharFilter(field_name='note', lookup_expr='icontains')

    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['customer', 'created_date']
