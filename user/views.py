from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import CityForm, FlightForm
from .models import Flight, City
from django.views.decorators.http import require_POST



#Личный кабинет
@login_required
def profile_view(request):
    if request.user.is_staff:  # админ
        return render(request, 'user/admin_profile.html')
    return render(request, 'user/user_profile.html')


#Страница управления рейсами (админ)
def airplan_view(request):
    return render(request, 'map/flights_manage.html')


#Просмотр рейсов на карте (для пользователей)
def flights_view(request):
    flights = Flight.objects.all()
    return render(request, "map/flights_view.html", {"flights": flights})


#Список городов (для админа)
def city_list(request):
    q = request.GET.get("q")
    if q:
        cities = City.objects.filter(name__icontains=q) | City.objects.filter(region__icontains=q)
    else:
        cities = City.objects.all()
    return render(request, 'redact/City_list.html', {"cities": cities})


#Карта рейсов (для пользователей)
def flights_map(request):
    flights = Flight.objects.select_related("origin", "destination").all()
    return render(request, "map/flights_map.html", {"flights": flights})


#Создание города (админ)
def city_create(request):
    if request.method == "POST":
        form = CityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("city_list")
    else:
        form = CityForm()
    return render(request, "redact/city_form.html", {"form": form})


#Создание рейса (админ)
def flight_create(request):
    if request.method == "POST":
        form = FlightForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("flights_manage")
    else:
        form = FlightForm()
    return render(request, "redact1/flight_form.html", {"form": form})


#Редактирование города (админ)
def city_update(request, pk):
    city = get_object_or_404(City, pk=pk)
    if request.method == "POST":
        form = CityForm(request.POST, instance=city)
        if form.is_valid():
            form.save()
            return redirect("city_list")
    else:
        form = CityForm(instance=city)
    return render(request, "redact/city_edit.html", {"form": form, "city": city})


#Редактирование рейса (админ)
def flight_update(request, pk):
    flight = get_object_or_404(Flight, pk=pk)
    if request.method == "POST":
        form = FlightForm(request.POST, instance=flight)
        if form.is_valid():
            form.save()
            return redirect("flights_manage")
    else:
        form = FlightForm(instance=flight)
    return render(request, "redact1/flight_edit.html", {"form": form, "flight": flight})


#Управление рейсами (админ)
def flight_manage(request):
    flights = Flight.objects.select_related("origin", "destination").all()
    return render(request, "redact1/flight_manage.html", {"flights": flights})


def city_delete(request, pk):
    city = get_object_or_404(City, pk=pk)
    if request.method == "POST":
        city.delete()
        return redirect("city_list")
    return render(request, "redact/city_confirm_delete.html", {"city": city})




@require_POST
def flight_delete(request, pk):
    flight = get_object_or_404(Flight, pk=pk)
    flight.delete()
    return redirect("flights_manage")


from django.contrib.auth.decorators import login_required
from .models import Booking

@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, "user/my_bookings.html", {"bookings": bookings})


from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def all_bookings(request):
    bookings = Booking.objects.select_related("user", "flight")
    return render(request, "user/all_bookings.html", {"bookings": bookings})

