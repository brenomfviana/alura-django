from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from school.models import Course


class CourseTestCase(APITestCase):
    def setUp(self):
        self.list_url = reverse("Courses-list")
        self.course1 = Course.objects.create(
            code="CTT1",
            description="Curso Teste 1",
            level="B",
        )
        self.course1 = Course.objects.create(
            code="CTT2",
            description="Curso Teste 2",
            level="I",
        )

    # def test_fail(self):
    #     self.fail("Test that fails.")

    def test_list_courses_get_request(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_course_post_request(self):
        data = {
            "code": "CTT3",
            "description": "Curso Teste 3",
            "level": "A",
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete_course_forbidden(self):
        response = self.client.delete("/courses/1/")
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_update_course_put_request(self):
        data = {
            "id": 1,
            "code": "CTT1",
            "description": "Curso Teste 1 atualizado",
            "level": "B",
        }
        response = self.client.put("/courses/1/", data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, data)
