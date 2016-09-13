from django.contrib import admin
from hello.models import Person


class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'sex',)

admin.site.register(Person,PersonAdmin)
