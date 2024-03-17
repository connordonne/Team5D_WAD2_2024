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
            'cuisine': 'Italian',
            'number_of_reviews': 53,
            'average_rating': 4.65
        },
        {
            'name': 'Taj Mahal Indian Restaurant',
            'address': '34 Queen Street, Manchester',
            'phone': '0161 987 6543',
            'website': 'https://www.tajmahalindian.co.uk',
            'openingTime': '17:30 - 22:30',
            'priceRange': '££',
            'cuisine': 'Indian',
            'number_of_reviews': 42,
            'average_rating': 3.12
        },
        {
            'name': 'Golden Dragon Chinese Cuisine',
            'address': '56 King Street, Birmingham',
            'phone': '0121 234 5678',
            'website': 'https://www.goldendragonchinese.co.uk',
            'openingTime': '11:00 - 22:00',
            'priceRange': '££',
            'cuisine': 'Chinese',
            'number_of_reviews': 81,
            'average_rating': 1.03
        },
        {
            'name': 'Siam Thai Kitchen',
            'address': '78 Prince Street, Glasgow',
            'phone': '0141 345 6789',
            'website': 'https://www.siamthaikitchen.co.uk',
            'openingTime': '18:00 - 23:30',
            'priceRange': '££',
            'cuisine': 'Thai',
            'number_of_reviews': 12,
            'average_rating': 1.62
        },
        {
            'name': 'El Mariachi Mexican Cantina',
            'address': '90 Duke Street, Bristol',
            'phone': '0117 890 1234',
            'website': 'https://www.elmariachimexican.co.uk',
            'openingTime': '12:00 - 21:00',
            'priceRange': '££',
            'cuisine': 'Mexican',
            'number_of_reviews': 99,
            'average_rating': 1
        },
        {
            'name': 'Sakura Japanese Dining',
            'address': '123 Princess Street, Cardiff',
            'phone': '029 4567 8901',
            'website': 'https://www.sakurajapanesedining.co.uk',
            'openingTime': '18:30 - 22:30',
            'priceRange': '£££',
            'cuisine': 'Japanese',
            'number_of_reviews': 1,
            'average_rating': 2
        },
        {
            'name': 'Olive Tree Greek Tavern',
            'address': '45 Market Street, Liverpool',
            'phone': '0151 234 5678',
            'website': 'https://www.olivetreegreektavern.co.uk',
            'openingTime': '17:00 - 23:00',
            'priceRange': '££',
            'cuisine': 'Greek',
            'number_of_reviews': 34,
            'average_rating': 5
        },
        {
            'name': 'Le Bistro Français',
            'address': '67 Rue Street, Edinburgh',
            'phone': '0131 345 6789',
            'website': 'https://www.lebistrofrancais.co.uk',
            'openingTime': '19:00 - 00:00',
            'priceRange': '£££',
            'cuisine': 'French',
            'number_of_reviews': 52,
            'average_rating': 3.62
        },
        {
            'name': 'Tapas y Vinos',
            'address': '89 Calle Street, Belfast',
            'phone': '028 9012 3456',
            'website': 'https://www.tapasyvinos.co.uk',
            'openingTime': '18:00 - 22:30',
            'priceRange': '££',
            'cuisine': 'Spanish',
            'number_of_reviews': 73,
            'average_rating': 2.99
        },
        {
            'name': 'Uncle Sam\'s Diner',
            'address': '101 Broadway, Leeds',
            'phone': '0113 678 9012',
            'website': 'https://www.unclesamsdiner.co.uk',
            'openingTime': '07:00 - 22:00',
            'priceRange': '£',
            'cuisine': 'American',
            'number_of_reviews': 71,
            'average_rating': 2.5
        },
        {
            'name': 'Mamma Mia Trattoria',
            'address': '45 Oak Avenue, Manchester',
            'phone': '0161 987 6543',
            'website': 'https://www.mammamiatrattoria.co.uk',
            'openingTime': '11:30 - 22:00',
            'priceRange': '£££',
            'cuisine': 'Italian',
            'number_of_reviews': 78,
            'average_rating': 4.75
        },

        {
            'name': 'Bella Napoli Ristorante',
            'address': '7 Vine Street, Edinburgh',
            'phone': '0131 876 5432',
            'website': 'https://www.bellanapoli-ristorante.com',
            'openingTime': '12:00 - 23:00',
            'priceRange': '£££',
            'cuisine': 'Italian',
            'number_of_reviews': 62,
            'average_rating': 4.55
        },

        {
            'name': 'Gusto Italiano',
            'address': '20 Market Square, Birmingham',
            'phone': '0121 765 4321',
            'website': 'https://www.gustoitaliano.com',
            'openingTime': '11:00 - 22:30',
            'priceRange': '£££',
            'cuisine': 'Italian',
            'number_of_reviews': 85,
            'average_rating': 4.80
        },

        {
            'name': 'Ristorante Veneto',
            'address': '33 Canal Road, Glasgow',
            'phone': '0141 654 3210',
            'website': 'https://www.ristoranteveneto.co.uk',
            'openingTime': '12:30 - 22:00',
            'priceRange': '£££',
            'cuisine': 'Italian',
            'number_of_reviews': 67,
            'average_rating': 4.70
        },

        {
            'name': 'Trattoria La Famiglia',
            'address': '10 Riverside Drive, Bristol',
            'phone': '0117 543 2109',
            'website': 'https://www.trattorialafamiglia.com',
            'openingTime': '12:00 - 22:30',
            'priceRange': '£££',
            'cuisine': 'Italian',
            'number_of_reviews': 58,
            'average_rating': 4.65
        },
        {
            'name': 'Le Petit Bistro',
            'address': '14 Rue de la Paix, Paris',
            'phone': '+33 1 23 45 67 89',
            'website': 'https://www.lepetitbistro-paris.com',
            'openingTime': '12:00 - 23:00',
            'priceRange': '£££',
            'cuisine': 'French',
            'number_of_reviews': 70,
            'average_rating': 4.75
        },

        {
            'name': 'La Brasserie Parisienne',
            'address': '25 Avenue des Champs-Élysées, Paris',
            'phone': '+33 1 98 76 54 32',
            'website': 'https://www.labrasserieparisienne.com',
            'openingTime': '11:30 - 22:30',
            'priceRange': '£££',
            'cuisine': 'French',
            'number_of_reviews': 65,
            'average_rating': 4.60
        },

        {
            'name': 'Chez Pierre',
            'address': '8 Rue de la République, Lyon',
            'phone': '+33 4 56 78 90 12',
            'website': 'https://www.chezpierre-lyon.com',
            'openingTime': '12:30 - 22:00',
            'priceRange': '£££',
            'cuisine': 'French',
            'number_of_reviews': 80,
            'average_rating': 4.80
        },

        {
            'name': 'Le Coq au Vin',
            'address': '5 Rue des Vignes, Bordeaux',
            'phone': '+33 5 67 89 01 23',
            'website': 'https://www.lecoqauvin-bordeaux.com',
            'openingTime': '12:00 - 23:00',
            'priceRange': '£££',
            'cuisine': 'French',
            'number_of_reviews': 75,
            'average_rating': 4.70
        },

        {
            'name': 'La Crêperie Bretonne',
            'address': '18 Rue de la Liberté, Nice',
            'phone': '+33 6 54 32 10 98',
            'website': 'https://www.lacreperiebretonne-nice.com',
            'openingTime': '11:00 - 22:30',
            'priceRange': '£££',
            'cuisine': 'French',
            'number_of_reviews': 58,
            'average_rating': 4.65
        },
        {
            'name': 'Thai Terrace',
            'address': '25 Queen Street, London',
            'phone': '020 1234 5678',
            'website': 'https://www.thaiterrace.co.uk',
            'openingTime': '12:00 - 22:30',
            'priceRange': '£££',
            'cuisine': 'Thai',
            'number_of_reviews': 70,
            'average_rating': 4.80
        },
        {
            'name': 'Siam Garden',
            'address': '15 Park Lane, Manchester',
            'phone': '0161 987 6543',
            'website': 'https://www.siamgarden.com',
            'openingTime': '11:30 - 23:00',
            'priceRange': '££',
            'cuisine': 'Thai',
            'number_of_reviews': 55,
            'average_rating': 4.60
        },
        {
            'name': 'Bangkok Street Food',
            'address': '7 Elm Street, Birmingham',
            'phone': '0121 876 5432',
            'website': 'https://www.bangkokstreetfood.co.uk',
            'openingTime': '12:00 - 22:00',
            'priceRange': '££',
            'cuisine': 'Thai',
            'number_of_reviews': 63,
            'average_rating': 4.70
        },
        {
            'name': 'Thai Orchid',
            'address': '33 Riverside Road, Glasgow',
            'phone': '0141 654 3210',
            'website': 'https://www.thaiorchid.co.uk',
            'openingTime': '12:30 - 22:30',
            'priceRange': '£££',
            'cuisine': 'Thai',
            'number_of_reviews': 68,
            'average_rating': 4.75
        },
        {
            'name': 'Sawasdee Thai Cuisine',
            'address': '10 High Street, Edinburgh',
            'phone': '0131 543 2109',
            'website': 'https://www.sawasdeethaicuisine.com',
            'openingTime': '12:00 - 23:00',
            'priceRange': '££',
            'cuisine': 'Thai',
            'number_of_reviews': 52,
            'average_rating': 4.55
        },
        {
            'name': 'Sushi Zen',
            'address': '25 Sakura Street, London',
            'phone': '020 1234 5678',
            'website': 'https://www.sushizen.co.uk',
            'openingTime': '12:00 - 22:30',
            'priceRange': '£££',
            'cuisine': 'Japanese',
            'number_of_reviews': 75,
            'average_rating': 4.85
        },
        {
            'name': 'Sakura Sushi Bar',
            'address': '15 Cherry Lane, Manchester',
            'phone': '0161 987 6543',
            'website': 'https://www.sakurasushibar.com',
            'openingTime': '11:30 - 23:00',
            'priceRange': '£££',
            'cuisine': 'Japanese',
            'number_of_reviews': 60,
            'average_rating': 4.70
        },
        {
            'name': 'Tokyo Teppanyaki',
            'address': '7 Bamboo Street, Birmingham',
            'phone': '0121 876 5432',
            'website': 'https://www.tokyoteppanyaki.co.uk',
            'openingTime': '12:00 - 22:00',
            'priceRange': '£££',
            'cuisine': 'Japanese',
            'number_of_reviews': 68,
            'average_rating': 4.75
        },
        {
            'name': 'Matsuri Japanese Cuisine',
            'address': '33 Hanami Road, Glasgow',
            'phone': '0141 654 3210',
            'website': 'https://www.matsurijapanesecuisine.co.uk',
            'openingTime': '12:30 - 22:30',
            'priceRange': '£££',
            'cuisine': 'Japanese',
            'number_of_reviews': 70,
            'average_rating': 4.80
        },
        {
            'name': 'Kiku Japanese Restaurant',
            'address': '10 Bonsai Avenue, Edinburgh',
            'phone': '0131 543 2109',
            'website': 'https://www.kikujapaneserestaurant.com',
            'openingTime': '12:00 - 23:00',
            'priceRange': '£££',
            'cuisine': 'Japanese',
            'number_of_reviews': 55,
            'average_rating': 4.65
        },
        {
            'name': 'El Rancho Grande',
            'address': '25 Sombrero Street, London',
            'phone': '020 1234 5678',
            'website': 'https://www.elranchogrande.co.uk',
            'openingTime': '12:00 - 22:30',
            'priceRange': '££',
            'cuisine': 'Mexican',
            'number_of_reviews': 80,
            'average_rating': 4.75
        },
        {
            'name': 'Taco Loco',
            'address': '15 Salsa Avenue, Manchester',
            'phone': '0161 987 6543',
            'website': 'https://www.tacoloco.com',
            'openingTime': '11:30 - 23:00',
            'priceRange': '££',
            'cuisine': 'Mexican',
            'number_of_reviews': 65,
            'average_rating': 4.60
        },
        {
            'name': 'La Cantina',
            'address': '7 Cactus Street, Birmingham',
            'phone': '0121 876 5432',
            'website': 'https://www.lacantina.com',
            'openingTime': '12:00 - 22:00',
            'priceRange': '££',
            'cuisine': 'Mexican',
            'number_of_reviews': 72,
            'average_rating': 4.70
        },
        {
            'name': 'Chilli Fiesta',
            'address': '33 Pepper Road, Glasgow',
            'phone': '0141 654 3210',
            'website': 'https://www.chillifiesta.co.uk',
            'openingTime': '12:30 - 22:30',
            'priceRange': '££',
            'cuisine': 'Mexican',
            'number_of_reviews': 69,
            'average_rating': 4.65
        },
        {
            'name': 'Hola Amigos',
            'address': '10 Nacho Lane, Edinburgh',
            'phone': '0131 543 2109',
            'website': 'https://www.holaamigos.com',
            'openingTime': '12:00 - 23:00',
            'priceRange': '££',
            'cuisine': 'Mexican',
            'number_of_reviews': 60,
            'average_rating': 4.55
        },
        {
            'name': 'The Burger Joint',
            'address': '25 Main Street, New York',
            'phone': '212-555-1234',
            'website': 'https://www.theburgerjoint.com',
            'openingTime': '11:00 - 22:00',
            'priceRange': '$$',
            'cuisine': 'American',
            'number_of_reviews': 90,
            'average_rating': 4.8
        },
        {
            'name': 'Pancake Palace',
            'address': '15 Maple Avenue, Chicago',
            'phone': '312-555-5678',
            'website': 'https://www.pancakepalace.com',
            'openingTime': '07:00 - 15:00',
            'priceRange': '$',
            'cuisine': 'American',
            'number_of_reviews': 70,
            'average_rating': 4.5
        },
        {
            'name': 'BBQ Heaven',
            'address': '7 Hickory Lane, Austin',
            'phone': '512-555-9012',
            'website': 'https://www.bbqheaven.com',
            'openingTime': '12:00 - 20:00',
            'priceRange': '$$',
            'cuisine': 'American',
            'number_of_reviews': 85,
            'average_rating': 4.7
        },
        {
            'name': 'Diner Deluxe',
            'address': '33 Elm Street, Los Angeles',
            'phone': '213-555-3456',
            'website': 'https://www.dinerdeluxe.com',
            'openingTime': '08:00 - 22:00',
            'priceRange': '$$',
            'cuisine': 'American',
            'number_of_reviews': 80,
            'average_rating': 4.6
        },
        {
            'name': 'Steakhouse Supreme',
            'address': '10 Oak Street, Miami',
            'phone': '305-555-7890',
            'website': 'https://www.steakhousesupreme.com',
            'openingTime': '17:00 - 23:00',
            'priceRange': '$$$',
            'cuisine': 'American',
            'number_of_reviews': 75,
            'average_rating': 4.9
        },
        {
            'name': 'Spice Palace',
            'address': '25 Masala Street, London',
            'phone': '020 1234 5678',
            'website': 'https://www.spicepalace.co.uk',
            'openingTime': '12:00 - 22:30',
            'priceRange': '££',
            'cuisine': 'Indian',
            'number_of_reviews': 85,
            'average_rating': 4.7
        },
        {
            'name': 'Tandoori Nights',
            'address': '15 Curry Lane, Manchester',
            'phone': '0161 987 6543',
            'website': 'https://www.tandoorinights.com',
            'openingTime': '11:30 - 23:00',
            'priceRange': '££',
            'cuisine': 'Indian',
            'number_of_reviews': 75,
            'average_rating': 4.6
        },
        {
            'name': 'Naan Stop',
            'address': '7 Papadum Street, Birmingham',
            'phone': '0121 876 5432',
            'website': 'https://www.naanstop.com',
            'openingTime': '12:00 - 22:00',
            'priceRange': '££',
            'cuisine': 'Indian',
            'number_of_reviews': 80,
            'average_rating': 4.8
        },
        {
            'name': 'Curry House',
            'address': '33 Chutney Road, Glasgow',
            'phone': '0141 654 3210',
            'website': 'https://www.curryhouse.co.uk',
            'openingTime': '12:30 - 22:30',
            'priceRange': '££',
            'cuisine': 'Indian',
            'number_of_reviews': 70,
            'average_rating': 4.5
        },
        {
            'name': 'Saffron Kitchen',
            'address': '10 Biryani Avenue, Edinburgh',
            'phone': '0131 543 2109',
            'website': 'https://www.saffronkitchen.com',
            'openingTime': '12:00 - 23:00',
            'priceRange': '££',
            'cuisine': 'Indian',
            'number_of_reviews': 65,
            'average_rating': 4.4
        },
        {
            'name': 'Olive Garden',
            'address': '25 Athena Street, Athens',
            'phone': '+30 210 1234567',
            'website': 'https://www.olivegarden.gr',
            'openingTime': '12:00 - 22:30',
            'priceRange': '€€',
            'cuisine': 'Greek',
            'number_of_reviews': 90,
            'average_rating': 4.8
        },
        {
            'name': 'Zorba Taverna',
            'address': '15 Parthenon Avenue, Thessaloniki',
            'phone': '+30 2310 987654',
            'website': 'https://www.zorbastaverna.gr',
            'openingTime': '11:30 - 23:00',
            'priceRange': '€€',
            'cuisine': 'Greek',
            'number_of_reviews': 80,
            'average_rating': 4.6
        },
        {
            'name': 'Mediterranean Breeze',
            'address': '7 Poseidon Street, Crete',
            'phone': '+30 2810 876543',
            'website': 'https://www.mediterraneanbreeze.gr',
            'openingTime': '12:00 - 22:00',
            'priceRange': '€€',
            'cuisine': 'Greek',
            'number_of_reviews': 85,
            'average_rating': 4.7
        },
        {
            'name': 'Santorini Sunset',
            'address': '33 Ouzo Road, Santorini',
            'phone': '+30 2286 543210',
            'website': 'https://www.santorinisunset.gr',
            'openingTime': '12:30 - 22:30',
            'priceRange': '€€€',
            'cuisine': 'Greek',
            'number_of_reviews': 95,
            'average_rating': 4.9
        },
        {
            'name': 'Mykonos Tavern',
            'address': '10 Cyclades Avenue, Mykonos',
            'phone': '+30 2289 012345',
            'website': 'https://www.mykonostavern.gr',
            'openingTime': '12:00 - 23:00',
            'priceRange': '€€',
            'cuisine': 'Greek',
            'number_of_reviews': 75,
            'average_rating': 4.5
        },
        {
            'name': 'Golden Dragon',
            'address': '25 Panda Street, Beijing',
            'phone': '+86 10 1234 5678',
            'website': 'https://www.goldendragon.com',
            'openingTime': '12:00 - 22:30',
            'priceRange': '¥¥',
            'cuisine': 'Chinese',
            'number_of_reviews': 85,
            'average_rating': 4.7
        },
        {
            'name': 'Lucky Bamboo',
            'address': '15 Dynasty Avenue, Shanghai',
            'phone': '+86 21 9876 5432',
            'website': 'https://www.luckybamboo.com',
            'openingTime': '11:30 - 23:00',
            'priceRange': '¥¥',
            'cuisine': 'Chinese',
            'number_of_reviews': 80,
            'average_rating': 4.6
        },
        {
            'name': 'Great Wall Restaurant',
            'address': '7 Forbidden City Road, Xian',
            'phone': '+86 29 8765 4321',
            'website': 'https://www.greatwallrestaurant.com',
            'openingTime': '12:00 - 22:00',
            'priceRange': '¥¥',
            'cuisine': 'Chinese',
            'number_of_reviews': 88,
            'average_rating': 4.8
        },
        {
            'name': 'Peking Duck House',
            'address': '33 Silk Road, Hangzhou',
            'phone': '+86 571 6543 2109',
            'website': 'https://www.pekingduckhouse.com',
            'openingTime': '12:30 - 22:30',
            'priceRange': '¥¥',
            'cuisine': 'Chinese',
            'number_of_reviews': 82,
            'average_rating': 4.7
        },
        {
            'name': 'Red Lantern',
            'address': '10 Lantern Lane, Chengdu',
            'phone': '+86 28 5432 1098',
            'website': 'https://www.redlantern.com',
            'openingTime': '12:00 - 23:00',
            'priceRange': '¥¥',
            'cuisine': 'Chinese',
            'number_of_reviews': 78,
            'average_rating': 4.5
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
            defaults={'cuisine': cuisine},
            number_of_reviews=restaurant['number_of_reviews'],
            average_rating=restaurant['average_rating']
        )

        print(r.name)

if __name__ == '__main__':
    print('Starting RateARant populate script...')
    populate()
