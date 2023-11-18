from animals.models import Animal
from animals.tests import *
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class AnimalsTestCase(LiveServerTestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--remote-debugging-port=9222")
        self.browser = webdriver.Chrome(
            "/home/breno/Desktop/Projects/Django/alura-django-tdd/chromedriver",
            chrome_options=chrome_options,
        )
        self.animal = Animal.objects.create(
            name="Leão",
            predator=True,
            poisonous=False,
            domestic=False,
        )

    def tearDown(self):
        self.browser.quit()

    def test_is_browser_opening(self):
        self.browser.get(self.live_server_url)

    def test_looking_for_animal(self):
        """
        Test if a user finds an animal in their research but decides not to adopt.

        Given:
            - A person who wants to adopt a new pet.
        When:
            - They search for an animal in our site.
        Then:
            - Return a list of animals.
        """
        # The person access the Animal Search site
        homepage = self.browser.get(self.live_server_url + "/")

        # They see in the site menu "Animal Search"
        brand_element = self.browser.find_element(By.CSS_SELECTOR, ".navbar")
        self.assertEqual("Busca Animal", brand_element.text)

        # They see a field to search for animals by name
        search_input = self.browser.find_element(By.CSS_SELECTOR, "input#search")
        self.assertEqual(search_input.get_attribute("placeholder"), "Exemplo: Leão")

        # They write "Lion" and click on the search button
        search_input.send_keys("Leão")

        self.browser.find_element(By.CSS_SELECTOR, "form button").click()

        # The site shows four characteristics of the searched animal
        characteristics = self.browser.find_elements(
            By.CSS_SELECTOR, ".result-description"
        )
        self.assertGreater(len(characteristics), 3)

        # They give up on adopting a lion
