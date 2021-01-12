from django.contrib import admin

from .models import TodoList, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'created', 'due_date', 'completed',)


admin.site.register(TodoList, TodoAdmin)
admin.site.register(Category, CategoryAdmin)
