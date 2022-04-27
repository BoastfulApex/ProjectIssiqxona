from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets, status
from rest_framework.response import Response


class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request, *args, **kwargs):
        products = []
        for i in self.queryset:
            s = {
                "name": i.name,
                'text': i.text,
                'image': i.ImageURL
            }
            products.append(s)

        return Response({'products': products})


class QuestionView(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class StoryView(viewsets.ModelViewSet):
    queryset = Stories.objects.all()
    serializer_class = StorySerializer

    def list(self, request, *args, **kwargs):
        list_story = self.queryset
        story = []
        for i in list_story:
            s = {
                "name": i.name,
                'text': i.text,
                'image': i.ImageURL
            }
            story.append(s)

        return Response({'stories': story})
