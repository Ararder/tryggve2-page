from django.contrib import admin

# Register your models here.

from .models import Person, Country, Icon

admin.site.register(Person)
admin.site.register(Country)
admin.site.register(Icon)