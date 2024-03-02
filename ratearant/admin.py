from django.contrib import admin
from ratearant.models import Cuisine, Restaurant, User, Review, Comment, Score

# Register your models here.

admin.site.register(Cuisine)
admin.site.register(Restaurant)
admin.site.register(User)
admin.site.register(Review)
admin.site.register(Comment)
admin.site.register(Score)