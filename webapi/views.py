from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from .models import Product


class ProductList(APIView):

    def get(self, request: Request):
        min_price = request.query_params.get('min_price')
        max_price = request.query_params.get('max_price')
        if min_price is not None:
            products = products.filter(price__gte=min_price)
        if max_price is not None:
            products = products.filter(price__lte=max_price)
        else:
            products = Product.objects.all()
        data = []
        for product in products:
            data.append({
                'id': product.id,
                'title': product.title,
                'price': product.price
            })
        return Response(data, status=status.HTTP_200_OK)

    def post(self, request):
        product = Product()
        product.title = request.data.get('title')
        product.price = request.data.get('price')
        product.save()
        return Response(status=status.HTTP_201_CREATED)


class ProductDetail(APIView):

    def get(self, request, id):
        product = Product.objects.get(id=id)
        data = {
            'id': product.id,
            'title': product.title,
            'price': product.price
        }
        return Response(data, status=status.HTTP_200_OK)
    
    def put(self, request, id):
        product = Product.objects.get(id=id)
        product.title = request.data.get('title')
        product.price = request.data.get('price')
        product.save()
        return Response(status=status.HTTP_200_OK)

    def delete(self, request, id):
        product = Product.objects.get(id=id)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
