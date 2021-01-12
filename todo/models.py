from django.db import models
from django.db.models import Model, CharField, TextField, DateField, ForeignKey, BooleanField, CASCADE
from django.utils import timezone


class Category(Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return f"${self.name}"


class TodoList(Model):
    title = CharField(max_length=100)
    content = TextField(blank=True)
    created = DateField(auto_now_add=True)
    due_date = DateField(default=timezone.now().strftime("%Y-%m-%d"))
    completed = BooleanField(default=False)

    category = ForeignKey(Category, on_delete=CASCADE)

    class Meta:
        verbose_name = "TodoList"
        verbose_name_plural = "TodoLists"
        ordering = ["-created"]

    def __str__(self):
        return f"${self.title} " \
               f"${self.content}, " \
               f"${self.created}:%Y-%m-%d %H:%M:%S%z, " \
               f"${self.due_date}:%Y-%m-%d %H:%M:%S%z, " \
               f"${self.completed}"
