from animals.models import Animal
from django.test import RequestFactory, TestCase


class AnimalModelTestCase(TestCase):
    def setUp(self):
        self.animal = Animal.objects.create(
            name="Leão",
            predator=True,
            poisonous=False,
            domestic=False,
        )

    def test_if_animal_exists(self):
        self.assertEqual(self.animal.name, "Leão")
        self.assertEqual(self.animal.predator, True)
        self.assertEqual(self.animal.poisonous, False)
        self.assertEqual(self.animal.domestic, False)
