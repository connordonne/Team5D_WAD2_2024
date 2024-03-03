from django.contrib import admin
from ratearant.models import Cuisine, Restaurant, User, Review, Comment, Score


# Register your models here.
# add the cuisineID on the admin page
class CuisineAdmin(admin.ModelAdmin):
    list_display = ('cuisineId', 'cuisineName')


class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('restaurantId', 'name')


admin.site.register(Cuisine, CuisineAdmin)
admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(User)
admin.site.register(Review)
admin.site.register(Comment)
admin.site.register(Score)
