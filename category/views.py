from django.shortcuts import render
from rest_framework import viewsets
from .models import Category
from .serializers import CategorySerializer
# Create your views here.


class JobCategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer