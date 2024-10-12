from rest_framework import serializers

from teste.models import Client, Product, Employee, Sale


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'modified_at', 'name', 'rg', 'cpf', 'age', 'active']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'modified_at', 'description', 'quantity', 'active']


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'modified_at', 'name', 'registraction', 'active']


class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = ['id', 'modified_at', 'nrf', 'employee', 'client', 'product', 'active']
