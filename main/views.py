from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html', {'title': 'Airport'})

def search(request):
    # Здесь можно обработать параметры из формы
    from_city = request.GET.get('from')
    to_city = request.GET.get('to')
    depart_date = request.GET.get('depart')
    return_date = request.GET.get('return')
    passengers = request.GET.get('passengers')
    flight_class = request.GET.get('class')
    direct_only = request.GET.get('direct') == 'on'

    context = {
        'from': from_city,
        'to': to_city,
        'depart': depart_date,
        'return': return_date,
        'passengers': passengers,
        'class': flight_class,
        'direct': direct_only,
    }

    return render(request, 'main/search.html', context)
