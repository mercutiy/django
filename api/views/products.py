from json import JSONDecodeError
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from api.models import Collection, Product
from api.serializers import ProductSerializer
import json

SIZE_FIELD = 'size'


@csrf_exempt
@api_view(['GET', 'POST'])
def products(request):
    if request.method == 'GET':
        if SIZE_FIELD in request.GET:
            return get_products(request.GET[SIZE_FIELD])
        else:
            return get_products()
    elif request.method == 'POST':
        return update_all(request.body)


@api_view(['GET'])
def product(request, sku):
    try:
        curr_product = Product.objects.get(sku=sku)
    except Product.DoesNotExist:
        return Response({'error': 'Product does not exist'}, status=status.HTTP_404_NOT_FOUND)
    serializer = ProductSerializer(curr_product, many=False)
    return Response({'data': serializer.data})


@api_view(['GET'])
def products_by_collect(request, collection):
    product_list = Product.objects.filter(collection=collection)
    if product_list.count() == 0:
        try:
            Collection.objects.get(collection=collection)
        except Collection.DoesNotExist:
            return Response({'error': 'Collection does not exist'}, status=status.HTTP_404_NOT_FOUND)
    serializer = ProductSerializer(product_list, many=True)
    return Response({'data': serializer.data})


def get_products(size=0):
    if size == 0:
        product_list = Product.objects.all()
    else:
        product_list = Product.objects.filter(size=size)
    serializer = ProductSerializer(product_list, many=True)
    return Response({'data': serializer.data})


def update_all(json_str):
    try:
        data = json.loads(json_str)
    except JSONDecodeError:
        return Response({'error': 'Malformed JSON provided'}, status.HTTP_400_BAD_REQUEST)

    for collection in data:
        collect_name = collection.get('collection', '').strip()
        prod_size = int(collection.get('size', 0))
        collect_products = collection.get('products', [])
        if collect_name == '' or prod_size == 0:
            return Response({'error': 'Wrong JSON structure'}, status.HTTP_400_BAD_REQUEST)
        collect = Collection(collection=collect_name)
        collect.save()
        for product in collect_products:
            prod_name = product.get('name', '').strip()
            prod_image = product.get('image', '').strip()
            prod_sku = product.get('sku', '').strip()
            if prod_name == '' or prod_image == '' or prod_sku == '':
                return Response({'error': 'Wrong JSON structure'}, status.HTTP_400_BAD_REQUEST)
            prod = Product(sku=prod_sku, name=prod_name, image=prod_image, size=prod_size, collection=collect)
            prod.save()
    return Response(status=status.HTTP_201_CREATED)