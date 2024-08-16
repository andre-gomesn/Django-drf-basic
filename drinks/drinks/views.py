from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializer

def drinks_page(request):
    drinks = Drink.objects.all()
    serializer = DrinkSerializer(drinks, many=True)
    return JsonResponse({'data': serializer.data}, safe=False)