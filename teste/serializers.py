from rest_framework import serializers

from teste.models import Cliente, Product, Sale, Employee


class ClientSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    name = serializers.CharField(read_only=True, max_length=80)
    age = serializers.IntegerField(read_only=True, min_value=0, max_value=100)

    class Meta:
        model = Cliente()
        fields = ['__all__']


class ProductSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    name = serializers.CharField(read_only=True, max_length=80)
    registration = serializers.CharField(read_only=True, max_length=15)

    class Meta:
        model = Product()
        fields = ['__all__']


class SaleSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    id_employee = serializers.IntegerField(read_only=True)
    id_cliente = serializers.IntegerField(read_only=True)
    id_product = serializers.IntegerField(read_only=True)

    class Meta:
        model = Sale()
        fields = ['__all__']


class EmployeeSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    name = serializers.CharField(read_only=True, max_length=80)

    class Meta:
        model = Employee
        fields = ['__all__']
