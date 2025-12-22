from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Flight, City


@login_required
def profile_view(request):
    if request.user.is_staff:  # админ
        return render(request, 'user/admin_profile.html')
    return render(request, 'user/user_profile.html')


def airplan_view(request):
    return render(request, 'user/flights_manage.html')



def flights_view(request):
    flights = Flight.objects.all()
    return render(request, "map/flights_view.html", {"flights": flights})

def City(request):
    return render(request, 'user/City_list.html')

def City_create(request):
    return render(request, 'user/City_list.html')

