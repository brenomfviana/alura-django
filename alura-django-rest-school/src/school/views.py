from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import generics, status, viewsets
from rest_framework.response import Response

from school.models import Course, Enrollment, Student
from school.serializers import (
    CourseSerializer,
    EnrollmentSerializer,
    StudentEnrollmentListSerializer,
    StudentsByCourseListSerializer,
    StudentSerializer,
    StudentSerializerV2,
)


class CreateResponseViewSet(viewsets.ModelViewSet):
    def create(self, request, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = Response(serializer.data, status=status.HTTP_201_CREATED)
            id = str(serializer.data["id"])
            response["Location"] = request.build_absolute_uri() + id
            return response


class StudentViewSet(CreateResponseViewSet):
    """Showing all students."""

    queryset = Student.objects.all()

    def get_serializer_class(self):
        if self.request.version == "v2":
            return StudentSerializerV2
        else:
            return StudentSerializer

    @method_decorator(cache_page(20))
    def dispatch(self, *args, **kwargs):
        return super(StudentViewSet, self).dispatch(*args, **kwargs)


class CourseViewSet(CreateResponseViewSet):
    """Showing all courses."""

    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    http_method_names = ["get", "post", "put", "patch"]

    @method_decorator(cache_page(20))
    def dispatch(self, *args, **kwargs):
        return super(CourseViewSet, self).dispatch(*args, **kwargs)


class EnrollmentViewSet(CreateResponseViewSet):
    """Showing all enrollments."""

    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    http_method_names = ["get", "post", "put", "patch"]

    @method_decorator(cache_page(20))
    def dispatch(self, *args, **kwargs):
        return super(EnrollmentViewSet, self).dispatch(*args, **kwargs)


class StudentEnrollmentListViewSet(generics.ListAPIView):
    """Showing all enrollments of a student."""

    serializer_class = StudentEnrollmentListSerializer

    def get_queryset(self):
        queryset = Enrollment.objects.filter(student_id=self.kwargs["pk"])
        return queryset

    @method_decorator(cache_page(20))
    def dispatch(self, *args, **kwargs):
        return super(StudentEnrollmentListViewSet, self).dispatch(*args, **kwargs)


class StudentsByCourseListViewSet(generics.ListAPIView):
    """Showing all students of a course."""

    serializer_class = StudentsByCourseListSerializer

    def get_queryset(self):
        queryset = Enrollment.objects.filter(course_id=self.kwargs["pk"])
        return queryset

    @method_decorator(cache_page(20))
    def dispatch(self, *args, **kwargs):
        return super(StudentsByCourseListViewSet, self).dispatch(*args, **kwargs)
