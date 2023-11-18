from rest_framework import serializers

from school.models import Course, Enrollment, Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ["id", "name", "cpf", "birthdate", "picture"]


class StudentSerializerV2(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ["id", "name", "cellphone", "cpf", "birthdate", "picture"]


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        exclude = []


class StudentEnrollmentListSerializer(serializers.ModelSerializer):

    course = serializers.ReadOnlyField(source="course.description")
    shift = serializers.SerializerMethodField()

    class Meta:
        model = Enrollment
        fields = ["course", "shift"]

    def get_shift(self, obj):
        return obj.get_shift_display()


class StudentsByCourseListSerializer(serializers.ModelSerializer):

    student = serializers.ReadOnlyField(source="student.name")

    class Meta:
        model = Enrollment
        fields = ["student"]
