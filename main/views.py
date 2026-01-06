from .forms import FlightSearchForm
from user.models import Flight, Booking
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages



def filter_flights(form):
    # Если форма не отправлена или невалидна — ничего не показываем
    if not form.is_valid():
        return None

    origin = form.cleaned_data.get('origin')
    destination = form.cleaned_data.get('destination')

    # Поиск только если указаны оба города
    if not origin or not destination:
        return None

    flights = Flight.objects.all()

    passengers = form.cleaned_data.get('passengers')
    class_type = form.cleaned_data.get('class_type')
    depart_date = form.cleaned_data.get('depart_date')

    # Обязательные фильтры
    flights = flights.filter(
        origin__name__icontains=origin,
        destination__name__icontains=destination
    )

    # Дополнительные фильтры
    if passengers:
        flights = flights.filter(seats_available__gte=passengers)

    if class_type:
        flights = flights.filter(class_type=class_type)

    if depart_date:
        flights = flights.filter(departure_time__date=depart_date)

    return flights


def index(request):
    form = FlightSearchForm(request.GET or None)
    flights = filter_flights(form)

    return render(request, 'main/index.html', {
        'form': form,
        'flights': flights
    })


def search(request):
    form = FlightSearchForm(request.GET or None)
    flights = filter_flights(form)

    return render(request, 'main/search.html', {
        'form': form,
        'flights': flights
    })




def book_flight(request, pk):
    flight = get_object_or_404(Flight, pk=pk)

    if request.method == "POST":
        tickets = int(request.POST.get("tickets", 1))

        if tickets <= flight.seats_available:
            flight.seats_available -= tickets
            flight.save()

            Booking.objects.create(
                user=request.user,
                flight=flight,
                tickets=tickets
            )

            messages.success(request, f"Вы зарегистрировали {tickets} билет(ов) на рейс {flight.airline}.")
        else:
            messages.error(request, "Недостаточно свободных мест.")

    return redirect("search")




