from animals.views import index
from django.test import RequestFactory, TestCase


class AnimalsURLsTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_url_route_index_view(self):
        request = self.factory.get("/")
        with self.assertTemplateUsed("index.html"):
            response = index(request)
            self.assertEqual(response.status_code, 200)
