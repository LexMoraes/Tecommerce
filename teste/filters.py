from multiprocessing.connection import Client

from django_filters import rest_framework as filters

from teste.models import Product, Sale, Employee, Cliente

# Filtros de pesquisa
LIKE = 'unaccent__icontains'
EQUALS = 'exact'
STARTS_WITH = 'startswith'


class ClienteFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr=LIKE)
    rg = filters.CharFilter(lookup_expr=EQUALS)
    age = filters.CharFilter(lookup_expr=EQUALS)

    class Meta:
        model = Cliente
        fields = ['name', 'rg', 'age']


class ProductFilter(filters.FilterSet):
    description = filters.CharFilter(lookup_expr=LIKE)
    quanty = filters.CharFilter(lookup_expr=EQUALS)

    class Meta:
        model = Product
        fields = ['description', 'quanty']


class SaleFilter(filters.FilterSet):
    nrf = filters.CharFilter(lookup_expr=EQUALS)

    class Meta:
        model = Sale
        fields = ['nrf']


class EmployeeFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr=LIKE)
    registration = filters.CharFilter(lookup_expr=EQUALS)

    class Meta:
        model = Employee
        fields = ['name', 'registration']