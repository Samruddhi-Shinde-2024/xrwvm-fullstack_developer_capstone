# from django.contrib import admin
# from .models import related models


# Register your models here.

# CarModelInline class

# CarModelAdmin class

# CarMakeAdmin class with CarModelInline

# Register models here

from django.contrib import admin
from .models import CarMake, CarModel

# Inline class to show CarModel within CarMake
class CarModelInline(admin.TabularInline):
    model = CarModel
    extra = 1  # Number of empty CarModel forms to display

# Admin class for CarMake
class CarMakeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')  # Fields to display in admin list
    inlines = [CarModelInline]  # Add CarModel inline

# Admin class for CarModel
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'car_make', 'car_type', 'dealer_id', 'year')
    list_filter = ('car_make', 'car_type', 'year')
    search_fields = ('name',)

# Register models
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)
