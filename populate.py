import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "team5d.settings")
import django
django.setup()
from ratearant.models import Cuisine, Restaurant


def populate():
    cuisine_types = [
        {'name': 'Italian'},
        {'name': 'Indian'},
        {'name': 'Chinese'},
        {'name': 'Thai'},
        {'name': 'Mexican'},
        {'name': 'Japanese'},
        {'name': 'Greek'},
        {'name': 'French'},
        {'name': 'Spanish'},
        {'name': 'American'}
    ]

    restaurants = [
        {
            'name': 'Piazza Italia',
            'address': '12 High Street, London',
            'phone': '020 1234 5678',
            'website': 'https://www.piazzaitalia.co.uk',
            'openingTime': '12:00 - 23:00',
            'priceRange': '£££',
            'cuisine': 'Italian'
        },
        {
            'name': 'Taj Mahal Indian Restaurant',
            'address': '34 Queen Street, Manchester',
            'phone': '0161 987 6543',
            'website': 'https://www.tajmahalindian.co.uk',
            'openingTime': '17:30 - 22:30',
            'priceRange': '££',
            'cuisine': 'Indian'
        },
        {
            'name': 'Golden Dragon Chinese Cuisine',
            'address': '56 King Street, Birmingham',
            'phone': '0121 234 5678',
            'website': 'https://www.goldendragonchinese.co.uk',
            'openingTime': '11:00 - 22:00',
            'priceRange': '££',
            'cuisine': 'Chinese'
        },
        {
            'name': 'Siam Thai Kitchen',
            'address': '78 Prince Street, Glasgow',
            'phone': '0141 345 6789',
            'website': 'https://www.siamthaikitchen.co.uk',
            'openingTime': '18:00 - 23:30',
            'priceRange': '££',
            'cuisine': 'Thai'
        },
        {
            'name': 'El Mariachi Mexican Cantina',
            'address': '90 Duke Street, Bristol',
            'phone': '0117 890 1234',
            'website': 'https://www.elmariachimexican.co.uk',
            'openingTime': '12:00 - 21:00',
            'priceRange': '££',
            'cuisine': 'Mexican'
        },
        {
            'name': 'Sakura Japanese Dining',
            'address': '123 Princess Street, Cardiff',
            'phone': '029 4567 8901',
            'website': 'https://www.sakurajapanesedining.co.uk',
            'openingTime': '18:30 - 22:30',
            'priceRange': '£££',
            'cuisine': 'Japanese'
        },
        {
            'name': 'Olive Tree Greek Tavern',
            'address': '45 Market Street, Liverpool',
            'phone': '0151 234 5678',
            'website': 'https://www.olivetreegreektavern.co.uk',
            'openingTime': '17:00 - 23:00',
            'priceRange': '££',
            'cuisine': 'Greek'
        },
        {
            'name': 'Le Bistro Français',
            'address': '67 Rue Street, Edinburgh',
            'phone': '0131 345 6789',
            'website': 'https://www.lebistrofrancais.co.uk',
            'openingTime': '19:00 - 00:00',
            'priceRange': '£££',
            'cuisine': 'French'
        },
        {
            'name': 'Tapas y Vinos',
            'address': '89 Calle Street, Belfast',
            'phone': '028 9012 3456',
            'website': 'https://www.tapasyvinos.co.uk',
            'openingTime': '18:00 - 22:30',
            'priceRange': '££',
            'cuisine': 'Spanish'
        },
        {
            'name': 'Uncle Sam\'s Diner',
            'address': '101 Broadway, Leeds',
            'phone': '0113 678 9012',
            'website': 'https://www.unclesamsdiner.co.uk',
            'openingTime': '07:00 - 22:00',
            'priceRange': '£',
            'cuisine': 'American'
        }
    ]

    reviews=[
        {

        }

    ]


    add_cuisine(cuisine_types)
    add_restaurant(restaurants)


def add_cuisine(cuisine_type):
    for cuisine in cuisine_type:
        c = Cuisine.objects.get_or_create(cuisineName=cuisine['name'])[0]
        c.save()


def add_restaurant(restaurants):
    for restaurant in restaurants:
        cuisine_type = restaurant['cuisine']
        cuisine, created = Cuisine.objects.get_or_create(cuisineName=cuisine_type)
        # Create or get the restaurant object
        r, created = Restaurant.objects.get_or_create(
            name=restaurant['name'],
            address=restaurant['address'],
            phone=restaurant['phone'],
            website=restaurant['website'],
            openingTime=restaurant['openingTime'],
            priceRange=restaurant['priceRange'],
            defaults={'cuisine': cuisine}
        )

        print(r.name)


if __name__ == '__main__':
    print('Starting RateARant populate script...')
    populate()
