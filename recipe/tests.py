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
