from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from SAIU_DATOS.models import Info
# Register your models here.

class extraInfor(admin.ModelAdmin):
    list_display = ("name", "description")

admin.site.register(Info)


# admin.site.register(User, UserAdmin)