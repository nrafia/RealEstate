from django.contrib import admin

from .models import Property, States, Reserve

admin.site.register(States)
admin.site.register(Reserve)


class PropertyAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'state', 'price', 'ads_id', 'featured')
    ordering = ('name',)
    search_fields = ('ads_id',)


admin.site.register(Property, PropertyAdmin)
