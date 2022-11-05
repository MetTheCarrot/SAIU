from django.contrib import admin

from SAIU_DATOS.models import Agosto, Septiembre, Octubre, Noviembre
# Register your models here.

# class extraInfor(admin.ModelAdmin):
#     list_display = ("name", "description")

admin.site.register(Agosto)
admin.site.register(Septiembre)
admin.site.register(Octubre)
admin.site.register(Noviembre)
