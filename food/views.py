from django.shortcuts import render
from .models import Restaurant

def food_view(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'food/food_view.html', {"restaurants": restaurants})
