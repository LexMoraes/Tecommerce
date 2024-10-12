from django.db.models.lookups import IContains
from django_filters import rest_framework as filters

from teste import models

# Filtros de pesquisa
LIKE = 'unaccent__icontains'
ICONTAINS = 'icontains'
EQUALS = 'exact'

STARTS_WITH = 'startswith'


class ClientFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr=ICONTAINS)
    cpf = filters.CharFilter(lookup_expr=STARTS_WITH)
    rg = filters.CharFilter(lookup_expr=STARTS_WITH)
    age = filters.NumberFilter(lookup_expr=EQUALS)

    class Meta:
        model = models.Client
        fields = ['name', 'cpf', 'rg', 'age']


class ProductFilter(filters.FilterSet):
    description = filters.CharFilter(lookup_expr=ICONTAINS)
    quantity = filters.NumberFilter(lookup_expr=EQUALS)

    class Meta:
        model = models.Product
        fields = ['description', 'quantity']


class EmployeeFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr=ICONTAINS)
    registration = filters.CharFilter(lookup_expr=EQUALS)

    class Meta:
        model = models.Employee
        fields = ['name', 'registration']


class SaleFilter(filters.FilterSet):
    nrf = filters.CharFilter(lookup_expr=EQUALS)
    employee = filters.CharFilter(field_name='employee__name', lookup_expr=ICONTAINS)
    registration__employee = filters.CharFilter(field_name='employee__registration', lookup_expr=EQUALS)
    client = filters.CharFilter(field_name='client__name',lookup_expr=ICONTAINS)
    cpf_cliente = filters.CharFilter(field_name='client__cpf', lookup_expr=STARTS_WITH)
    product = filters.CharFilter(field_name='product__description',lookup_expr=ICONTAINS)

    class Meta:
        model = models.Sale
        fields = ['nrf', 'employee', 'client', 'product']


