from customers.models import Customer
from customers.validators import *
from rest_framework import serializers
from rest_framework.serializers import ValidationError


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"

    def validate(self, data):
        errors = {}
        if not is_cpf_valid(data["cpf"]):
            errors["cpf"] = "O CPF é inválido!"

        if not is_name_valid(data["name"]):
            errors["name"] = "Não inclua números no campo nome!"

        if not is_cellphone_valid(data["cellphone"]):
            errors["cellphone"] = (
                "O número do celular deve seguir" "este modelo: 84 91234-1234!"
            )

        if errors:
            raise ValidationError(errors)

        return data
