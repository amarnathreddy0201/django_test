from django.contrib import admin


from .models import Files
class FileAdmin(admin.ModelAdmin):
    list_display = ["BANKNIFTY","DATE","TIME","OPEN","HIGH","LOW","CLOSE","VOLUME"]
admin.site.register(Files)