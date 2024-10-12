from django.db import models


class ModelBase(models.Model):
    id = models.BigAutoField(
        db_column='id',
        null=False,
        primary_key=True,
    )
    created_at = models.DateTimeField(
        db_column='dt_created_at',
        auto_now_add=True,
        null=False,
    )
    modified_at = models.DateTimeField(
        db_column='dt_modified_at',
        auto_now=True,
        null=False,
    )
    active = models.BooleanField(
        db_column='cs_active',
        default=True,
        null=False,
    )

    class Meta:
        abstract = True #dizendo que é uma classe abstrata
        managed = True


class Product(ModelBase):
    description = models.TextField(
        db_column='tx_description',
        null=False,
    )

    quantity = models.IntegerField(
        db_column='nb_quantity',
        null=False,
        default=0,
    )


class Client(ModelBase):
    name = models.CharField(
        db_column='tx_name',
        max_length=70,
        null=False,
    )

    age = models.IntegerField(
        db_column='nb_age',
        null=False,
    )

    rg = models.CharField(
        db_column='tx_rg',
        max_length=12,
        null=False,
    )

    cpf = models.CharField(
        db_column='tx_cpf',
        max_length=12,
        null=False,
    )


class Employee(ModelBase):
    name = models.CharField(
        db_column='tx_name',
        max_length=70,
        null=False,
    )

    registraction = models.CharField(
        db_column='tx_registraction',
        max_length=15,
        null=False,
    )


class Sale(ModelBase):
    nrf = models.CharField(
        db_column='tx_nrf',
        null=False,
        max_length=255,
    )

    employee = models.ForeignKey(
        Employee,
        db_column='id_employee',
        null=False,
        on_delete=models.DO_NOTHING,
    )

    client = models.ForeignKey(
        Client,
        db_column='id_client',
        null=False,
        on_delete=models.DO_NOTHING,
    )

    product = models.ForeignKey(
        Product,
        db_column='id_product',
        null=False,
        on_delete=models.DO_NOTHING,
    )



