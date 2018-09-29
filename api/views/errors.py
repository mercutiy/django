from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@csrf_exempt
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def error404(request):
    return Response(status=status.HTTP_404_NOT_FOUND);
