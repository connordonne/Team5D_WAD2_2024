from django.contrib import admin
from ratearant.models import Cuisine, Restaurant, Review, UserProfile

# add the cuisineID on the admin page
class CuisineAdmin(admin.ModelAdmin):
    list_display = ('cuisineId', 'cuisineName')

# add the slug on the admin page
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('restaurantId', 'name')
    prepopulated_fields = {'slug': ('name',)}

# register the models
admin.site.register(Cuisine, CuisineAdmin)
admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Review)
admin.site.register(UserProfile)