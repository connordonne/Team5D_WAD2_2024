from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse, resolve

from django.contrib.auth.models import User
from .models import Cuisine, Restaurant, Review
from .forms import UserForm, ReviewForm
from ratearant import views

class CuisineModelTest(TestCase):
    def setUp(self):
        Cuisine.objects.create(cuisineName='Italian')

    def test_cuisine_str(self):
        cuisine = Cuisine.objects.get(cuisineName='Italian')
        self.assertEqual(str(cuisine), 'Italian')

class RestaurantModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.cuisine = Cuisine.objects.create(cuisineName='Mexican')

        Restaurant.objects.create(
            name='El Pueblo',
            address='123 Taco Street',
            phone='555-1234',
            website='http://elpueblo.example.com',
            openingTime='9:00 AM - 9:00 PM',
            priceRange='$$',
            cuisine=cls.cuisine,
        )

    def test_restaurant_creation(self):
        restaurant = Restaurant.objects.get(name='El Pueblo')
        self.assertEqual(restaurant.name, 'El Pueblo')

    def test_restaurant_str(self):
        restaurant = Restaurant.objects.get(name='El Pueblo')
        self.assertEqual(str(restaurant), 'El Pueblo')

    def test_slug_creation_on_save(self):
        restaurant = Restaurant.objects.get(name='El Pueblo')
        self.assertEqual(restaurant.slug, 'el-pueblo')

class ViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.cuisine = Cuisine.objects.create(cuisineName='Italian')
        self.restaurant = Restaurant.objects.create(
            name='Test Restaurant',
            address='123 Test St',
            phone='123-456-7890',
            website='http://www.testrestaurant.com',
            openingTime='9:00 AM - 9:00 PM',
            priceRange='$$',
            cuisine=self.cuisine
        )
        
    def test_home_view(self):
        response = self.client.get(reverse('ratearant:home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ratearant/home.html')
        self.assertTrue('restaurants' in response.context)
    
    def test_about_view(self):
        response = self.client.get(reverse('ratearant:about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ratearant/about.html')

    def test_show_restaurant_view(self):
        slug = self.restaurant.slug
        response = self.client.get(reverse('ratearant:show_restaurant', kwargs={'restaurant_name_slug': slug}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ratearant/restaurant.html')
        self.assertTrue('restaurant' in response.context)

    def test_login_view_post(self):
        response = self.client.post(reverse('ratearant:login'), {'username': 'testuser', 'password': '12345'})
        self.assertRedirects(response, reverse('ratearant:home'))

    def test_login_view_get(self):
        response = self.client.get(reverse('ratearant:login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ratearant/login.html')

class UserFormTest(TestCase):
    def test_userform_valid_data(self):
        form = UserForm(data={
            'username': 'testuser',
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'testuser@example.com',
            'password': 'testpassword123',
        })
        self.assertTrue(form.is_valid())

    def test_userform_no_data(self):
        form = UserForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 4)  

class ReviewFormTest(TestCase):
    def test_reviewform_valid_data(self):
        form = ReviewForm(data={
            'foodRating': 5,
            'serviceRating': 4,
            'overallRating': 5,
            'message': 'Great experience!',
        })
        self.assertTrue(form.is_valid())

    def test_reviewform_invalid_data(self):
        form = ReviewForm(data={
            'foodRating': 6,  
            'serviceRating': 'excellent',  
            'overallRating': 0,  
            'message': '',
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 4)  

class TestUrls(SimpleTestCase):
    def test_home_url_resolves(self):
        url = reverse('ratearant:home')
        self.assertEquals(resolve(url).func, views.home)

    def test_about_url_resolves(self):
        url = reverse('ratearant:about')
        self.assertEquals(resolve(url).func, views.about)

    def test_register_url_resolves(self):
        url = reverse('ratearant:register')
        self.assertEquals(resolve(url).func, views.register)

    def test_login_url_resolves(self):
        url = reverse('ratearant:login')
        self.assertEquals(resolve(url).func, views.login_view)

    def test_logout_url_resolves(self):
        url = reverse('ratearant:logout')
        self.assertEquals(resolve(url).func, views.user_logout)

    def test_show_restaurant_url_resolves(self):
        url = reverse('ratearant:show_restaurant', kwargs={'restaurant_name_slug': 'some-slug'})
        self.assertEquals(resolve(url).func, views.show_restaurant)

    def test_trending_url_resolves(self):
        url = reverse('ratearant:trending')
        self.assertEquals(resolve(url).func, views.trending)

    def test_add_review_url_resolves(self):
        url = reverse('ratearant:add_review', kwargs={'restaurant_name_slug': 'some-slug'})
        self.assertEquals(resolve(url).func, views.add_review)

    def test_food_styles_url_resolves(self):
        url = reverse('ratearant:food_styles')
        self.assertEquals(resolve(url).func, views.food_styles)

    def test_categories_url_resolves(self):
        url = reverse('ratearant:categories', kwargs={'cuisineName': 'italian'})
        self.assertEquals(resolve(url).func, views.categories)