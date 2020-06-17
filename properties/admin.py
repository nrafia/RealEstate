from django.contrib import admin

from .models import Property, States, Reserve

admin.site.register(Property)
admin.site.register(States)
admin.site.register(Reserve)