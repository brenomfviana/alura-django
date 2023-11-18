from animals.models import Animal
from django.db.models.query import QuerySet
from django.test import RequestFactory, TestCase


class IndexViewTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.animal = Animal.objects.create(
            name="Calopsita",
            predator=False,
            poisonous=False,
            domestic=True,
        )

    def test_index_view_search_result(self):
        animal = "Calopsita"
        context = {"search": animal}

        response = self.client.get("/", context)
        self.assertIs(type(response.context["characteristics"]), QuerySet)

        characteristics = response.context["characteristics"]
        self.assertEqual(animal, characteristics[0].name)
