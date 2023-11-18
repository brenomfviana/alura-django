from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=30)
    cpf = models.CharField(max_length=11)
    birthdate = models.DateField()
    cellphone = models.CharField(max_length=11, default="")
    picture = models.ImageField(blank=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    LEVEL = (
        ("B", "Basic"),
        ("I", "Intermediate"),
        ("A", "Advanced"),
    )
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=100)
    level = models.CharField(
        max_length=1, choices=LEVEL, blank=False, null=False, default="B"
    )

    def __str__(self):
        return self.description


class Enrollment(models.Model):
    SHIFT = (
        ("M", "Morning"),
        ("A", "Afternoon"),
        ("N", "Night"),
    )
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    shift = models.CharField(
        max_length=1, choices=SHIFT, blank=False, null=False, default="M"
    )
