from .forms import FlightSearchForm
from user.models import Flight, Booking
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages


# Проверка формы поиска
def filter_flights(form):
    if not form.is_valid():
        return None
    # откуда
    origin = form.cleaned_data.get('origin')
    # куда
    destination = form.cleaned_data.get('destination')

    # Показ рейсов если оба города написаны правильно
    if not origin or not destination:
        return None

    flights = Flight.objects.all()
    # Колво пассажир
    passengers = form.cleaned_data.get('passengers')
    # классы - об. биз.
    class_type = form.cleaned_data.get('class_type')
    # по дате
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

# главная страница
def index(request):
    form = FlightSearchForm(request.GET or None)
    flights = filter_flights(form)

    return render(request, 'main/index.html', {
        'form': form,
        'flights': flights
    })

#страница поиска рейсов
def search(request):
    form = FlightSearchForm(request.GET or None)
    flights = filter_flights(form)

    return render(request, 'main/search.html', {
        'form': form,
        'flights': flights
    })



# Находим рейс по ID или (особому ключу)
def book_flight(request, pk):
    flight = get_object_or_404(Flight, pk=pk)

    if request.method == "POST":
        # Колво билет
        tickets = int(request.POST.get("tickets", 1))

        if tickets <= flight.seats_available:
            # проверка мест
            flight.seats_available -= tickets
            flight.save()
            # Запись
            Booking.objects.create(
                user=request.user,
                flight=flight,
                tickets=tickets
            )

            messages.success(request, f"Вы зарегистрировали {tickets} билет(ов) на рейс {flight.airline}.")
        else:
            messages.error(request, "Недостаточно свободных мест.")

    return redirect("search")




