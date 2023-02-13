from django.contrib import admin

from .models import User, Todo



@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'password', 'todos']
    list_display_links = ['todos']


    def todos(self, *args):
        return [i for i in Todo.objects.all()]

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ['text', 'is_done', 'user']
