from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from . import models, serializers
import random


class CategoryList(generics.ListAPIView):
    serializer_class = serializers.CategorySerializer
    queryset = models.Category.objects.all()

class HomeCategoryList(generics.ListAPIView):
    serializer_class = serializers.CategorySerializer

    def get_queryset(self):
        queryset = models.Category.objects.all()
        queryset = list(queryset)
        random.shuffle(queryset)
        return queryset[:5]

class PopularProductsList(generics.ListAPIView):
    serializer_class = serializers.ProductSerializer

    def get_queryset(self):
        queryset = models.Product.objects.filter(ratings__gte=4.0, ratings__lte=5.0)
        queryset = list(queryset)
        random.shuffle(queryset)
        return queryset[:20]

class ProductList(generics.ListAPIView):
    serializer_class = serializers.ProductSerializer

    def get_queryset(self):
        queryset = models.Product.objects.all()
        queryset = list(queryset)
        random.shuffle(queryset)
        return queryset[:20]

class SimilarProducts(APIView):
    def get(self, request):
        query = request.query_params.get('category', None)
        if query:
            products = models.Product.objects.filter(category__id=query)
            product_list = list(products)
            random.shuffle(product_list)
            limited_products = product_list[:6]
            serializer = serializers.ProductSerializer(limited_products, many=True)
            return Response(serializer.data)
        else:
            return Response({'message': "No query provided"}, status=status.HTTP_400_BAD_REQUEST)

class SearchProductByTitle(APIView):
    def get(self, request):
        query = request.query_params.get('q', None)
        if query:
            products = models.Product.objects.filter(title__icontains=query)
            serializer = serializers.ProductSerializer(products, many=True)
            return Response(serializer.data)
        else:
            return Response({'message': "No query provided"}, status=status.HTTP_400_BAD_REQUEST)

class FilterProductByCategory(APIView):
    def get(self, request):
        query = request.query_params.get('category', None)
        if query:
            products = models.Product.objects.filter(category__id=query)
            serializer = serializers.ProductSerializer(products, many=True)
            return Response(serializer.data)
        else:
            return Response({'message': "No query provided"}, status=status.HTTP_400_BAD_REQUEST)