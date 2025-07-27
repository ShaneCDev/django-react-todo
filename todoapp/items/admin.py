from django.contrib import admin

from .models import Item


class TodoItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'completed', 'created_at', 'updated_at')


# Register your models here.
admin.site.register(Item, TodoItemAdmin)