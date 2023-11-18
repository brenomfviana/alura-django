from django.test import TestCase

from aluraflix.models import Program


class ProgramModelTestCase(TestCase):
    def setUp(self):
        self.program = Program(
            title="Procurando ninguém em latim",
            release_date="2003-07-04",
        )

    def test_program_attributes(self):
        """Test to check the default values of program attributes"""
        self.assertEqual(self.program.title, "Procurando ninguém em latim")
        self.assertEqual(self.program.type, "M")
        self.assertEqual(self.program.release_date, "2003-07-04")
        self.assertEqual(self.program.likes, 0)
        self.assertEqual(self.program.dislikes, 0)
