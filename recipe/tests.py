from django.test import TestCase, Client
from .models import Recipe, Category

# Create your tests here.
class ViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_main_view(self):
        # Створення тестових рецептів
        category = Category.objects.create(name="Test Category")
        for i in range(6):
            Recipe.objects.create(title=f"Test Recipe {i}", description="Test Description",
                                  instructions="Test Instructions", ingredients="Test Ingredients",
                                  category=category)

        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['recipes']), 5)

    def test_category_list_view(self):
        # Створення тестових категорій
        for i in range(5):
            category = Category.objects.create(name=f"Test Category {i}")
            for j in range(i+1):
                Recipe.objects.create(title=f"Test Recipe {j}", description="Test Description",
                                      instructions="Test Instructions", ingredients="Test Ingredients",
                                      category=category)

        response = self.client.get('/categories/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['categories']), Category.objects.count())

        for category in response.context['categories']:
            self.assertEqual(category.recipe_count, Recipe.objects.filter(category=category).count())
