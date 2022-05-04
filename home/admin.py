from .models import Car, Profile
from django.contrib import admin
from django.utils.html import format_html


# Register your models here.


class CarAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}"width="250" height="150" />'.format(obj.image.url))

    image_tag.short_description = 'Image'

    list_display = ['image_tag', 'name']


admin.site.register(Car, CarAdmin)
admin.site.register(Profile)

