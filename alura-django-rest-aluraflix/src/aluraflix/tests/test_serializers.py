from django.test import TestCase

from aluraflix.models import Program
from aluraflix.serializers import ProgramSerializer


class ProgramModelTestCase(TestCase):
    def setUp(self):
        self.program = Program(
            title="Procurando ninguém em latim",
            release_date="2003-07-04",
            type="M",
            likes=2340,
            dislikes=40,
        )
        self.serializer = ProgramSerializer(instance=self.program)

    def test_serialized_fields(self):
        """Test to check if the fields are being serialized"""
        data = self.serializer.data
        self.assertEquals(
            set(data.keys()),
            set(["title", "type", "release_date", "likes"]),
        )

    def test_serialized_content(self):
        """Test to check the content of the serialized fields"""
        data = self.serializer.data
        self.assertEqual(data["title"], self.program.title)
        self.assertEqual(data["type"], self.program.type)
        self.assertEqual(data["release_date"], self.program.release_date)
        self.assertEqual(data["likes"], self.program.likes)
        with self.assertRaises(KeyError):
            data["dislikes"]
