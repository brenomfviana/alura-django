from django.contrib import admin

from school.models import Course, Enrollment, Student


class StudentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "cpf",
        "birthdate",
    )
    list_display_links = (
        "id",
        "name",
    )
    search_fields = ("name",)
    list_per_page = 20


class CourseAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "code",
        "description",
    )
    list_display_links = (
        "id",
        "code",
    )
    search_fields = ("code",)
    list_per_page = 20


class EnrollmentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "student",
        "course",
    )
    list_display_links = ("id",)
    list_per_page = 20


admin.site.register(Student, StudentAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Enrollment, EnrollmentAdmin)
