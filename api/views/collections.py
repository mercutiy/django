from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import Collection
from api.serializers import CollectionSerializer


@api_view(['GET'])
def all_collections(request):
    product_list = Collection.objects.all()
    serializer = CollectionSerializer(product_list, many=True)
    return Response({'data': serializer.data})
