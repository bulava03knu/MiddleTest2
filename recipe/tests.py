from django.test import TestCase, Client
from .models import Recipe, Category

# Create your tests here.


class ViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.category = Category.objects.create(name='Dessert')
        self.recipe = Recipe.objects.create(title='Chocolate Cake', description='Delicious chocolate cake', instructions='Bake it', ingredients='chocolate, flour, sugar, eggs', category=self.category)

    def test_main_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Chocolate Cake')

    def test_category_list_view(self):
        response = self.client.get('/categories/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Dessert')
