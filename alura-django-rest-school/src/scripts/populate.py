import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "setup.settings")
django.setup()

import random

from faker import Faker
from validate_docbr import CPF

from school.models import Course, Enrollment, Student


def create_students(amount):
    fake = Faker("pt_BR")
    Faker.seed(10)
    for _ in range(amount):
        cpf = CPF()
        name = fake.name()
        cpf = cpf.generate()
        birthdate = fake.date_between(start_date="-18y", end_date="today")
        student = Student(name=name, cpf=cpf, birthdate=birthdate)
        student.save()


def create_courses(amount):
    for _ in range(amount):
        code = "{}{}-{}".format(
            random.choice("ABCDEF"), random.randrange(10, 99), random.randrange(1, 9)
        )
        descs = [
            "Python Fundamentos",
            "Python intermediário",
            "Python Avançado",
            "Python para Data Science",
            "Python/React",
        ]
        description = random.choice(descs)
        descs.remove(description)
        level = random.choice("BIA")
        c = Course(code=code, description=description, level=level)
        c.save()


create_students(200)
create_courses(5)
