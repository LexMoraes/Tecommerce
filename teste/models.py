from django.db import models


class ModelBase(models.Model):
    id = models.BigAutoField(
        db_column='id',
        null=False,
        primary_key=True
    )
    created_at = models.DateTimeField(
        db_column='dt_created',
        auto_now_add=True,
        null=True
    )
    modified_at = models.DateTimeField(
        db_column='dt_modified',
        auto_now=True,
        null=True
    )
    active = models.BooleanField(
        db_column='cs_active',
        null=False,
        default=True
    )

    class Meta:
        abstract = True
        managed = True


class Cliente(ModelBase):
    name = models.CharField(
        db_column='tx_name',
        max_length=100)
    age = models.IntegerField(
        db_column='tx_age'
    )
    rg = models.CharField(
        max_length=12
    )
    cpf = models.CharField(
        max_length=12
    )


class Product(ModelBase):
    description = models.TextField(null=False)
    quantity = models.IntegerField(null=False)


class Employee(ModelBase):
    name = models.CharField(null=False, max_length=100)
    registration = models.CharField(null=False, max_length=100)


class Sale(ModelBase):
    nrf = models.CharField(null=False, max_length=255)
    id_employee = models.ForeignKey(Employee, null=False, on_delete=models.PROTECT)
    id_product = models.ForeignKey(Product, null=False, on_delete=models.PROTECT)
    id_cliente = models.ForeignKey(Cliente, null=False, on_delete=models.PROTECT)
