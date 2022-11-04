from django.contrib import admin

from SAIU_DATOS.models import Info, User
# Register your models here.

class extraInfor(admin.ModelAdmin):
    list_display = ("name", "description")

admin.site.register(Info)


