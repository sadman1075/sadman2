from django.contrib import admin
from .models import sadman

# Register your models here.


class sadmanadmin(admin.ModelAdmin):
    list_display=('username','city','thana','area','images')
admin.site.register(sadman,sadmanadmin)