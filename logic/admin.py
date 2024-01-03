from django.contrib import admin
from .models import Carousel, Category, List, List1, Team, Test, Contact
# Register your models here.

admin.site.register(Carousel)
admin.site.register(Category)
admin.site.register(List1)
admin.site.register(Test)
admin.site.register(Contact)

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('name',)}

@admin.register(List)
class ListAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('name',)}

