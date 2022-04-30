from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets, status
from rest_framework.response import Response


class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class QuestionView(viewsets.ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer


class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class LinkView(viewsets.ModelViewSet):
    queryset = Youtube.objects.all()
    serializer_class = LinkSerializer


class BlogView(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class ImageView(viewsets.ModelViewSet):
    queryset = BlogImage.objects.all()
    serializer_class = ImageSerializer


class PartnerView(viewsets.ModelViewSet):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer


class ImageByBlog(viewsets.ModelViewSet):
    queryset = BlogImage.objects.all()
    serializer_class = ImageSerializer

    def retrieve(self, request, *args, **kwargs):
        id = kwargs['pk']
        images = []
        blogs = self.queryset.filter(blog_id=id)
        serializer = self.get_serializer(blogs)
        for blog in blogs:
            kurs = {
                "id": blog.id,
                'Blog': blog.blog.id,
                'image': blog.ImageURL,
            }
            images.append(kurs)
        return Response({"Images": images})
