import re

from validate_docbr import CPF


def is_cpf_valid(cpf):
    return CPF().validate(cpf)


def is_name_valid(name):
    return name.isalpha()


def is_cellphone_valid(cellphone):
    """Validate cellphone (84 91234-1234)"""
    model = "[0-9]{2} [0-9]{5}-[0-9]{4}"
    response = re.findall(model, cellphone)
    return response
