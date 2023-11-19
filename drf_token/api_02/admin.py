from django.contrib import admin

# Register your models here.

from api_02 import models

admin.site.register(models.User)
admin.site.register(models.Book)
admin.site.register(models.Car)
