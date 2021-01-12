from django.apps import AppConfig
from django.db.models.signals import post_save, post_delete


class TodoConfig(AppConfig):
    name = 'todo'

    def ready(self):
        from .models import TodoList
        from .signals import (
            user_post_delete_handler,
            user_post_save_handler,
        )

        post_save.connect(user_post_save_handler, sender=TodoList)
        post_delete.connect(user_post_delete_handler, sender=TodoList)