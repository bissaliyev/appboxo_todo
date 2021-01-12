from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django.core.cache import cache
from rest_framework.viewsets import ModelViewSet

from .models import TodoList, Category
from .serializers import TodoListSerializer, CategorySerializer


@method_decorator(cache_page(60 * 60 * 2))
@method_decorator(vary_on_cookie)
class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    # def retrieve(self, request, pk=None, **kwargs):
    #     cache_key = f"category_{pk}"
    #
    #     data = cache.get(cache_key)
    #     if data:
    #         return Response(data)
    #
    #     response = super().retrieve(request, pk=pk)
    #     cache.set(cache_key, response.data)
    #     return response


@method_decorator(cache_page(60 * 60 * 2))
@method_decorator(vary_on_cookie)
class TodoListViewSet(ModelViewSet):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer

    # def retrieve(self, request, pk=None, **kwargs):
    #     cache_key = f"todo_{pk}"
    #
    #     data = cache.get(cache_key)
    #     if data:
    #         return Response(data)
    #
    #     response = super().retrieve(request, pk=pk)
    #     cache.set(cache_key, response.data)
    #     return response
