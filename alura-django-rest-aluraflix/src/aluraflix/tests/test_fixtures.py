from django.test import TestCase

from aluraflix.models import Program


class FixtureDataTestCase(TestCase):
    fixtures = ["programas_iniciais"]

    def test_fixture_loading(self):
        program = Program.objects.get(pk=1)
        all_programs = Program.objects.all()
        self.assertEqual(program.title, "Coisas bizarras")
        self.assertEqual(len(all_programs), 9)
