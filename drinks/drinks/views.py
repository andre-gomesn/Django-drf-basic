from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def drinks_page(request):
    if request.method == 'GET':
        drinks = Drink.objects.all()
        serializer = DrinkSerializer(drinks, many=True)
        return JsonResponse({'data': serializer.data})
    
    if request.method == 'POST':
        serializer = DrinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)