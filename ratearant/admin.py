from django.contrib import admin
from ratearant.models import Cuisine, Restaurant, User, Review, Comment, Score, TopRatedRestaurant, \
    YourTopRatedRestaurant

# user login and logout
from ratearant.models import UserProfile


# Register your models here.
# add the cuisineID on the admin page
class CuisineAdmin(admin.ModelAdmin):
    list_display = ('cuisineId', 'cuisineName')


class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('restaurantId', 'name')
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Cuisine, CuisineAdmin)
admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(TopRatedRestaurant)
admin.site.register(YourTopRatedRestaurant)
admin.site.register(Review)
admin.site.register(Comment)
admin.site.register(Score)

# user login and logout
admin.site.register(UserProfile)
