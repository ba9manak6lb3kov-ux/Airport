from django import forms

class FlightSearchForm(forms.Form):
    origin = forms.CharField(required=False, label="Откуда")
    destination = forms.CharField(required=False, label="Куда")
    passengers = forms.IntegerField(required=False, min_value=1, label="Количество пассажиров")
    class_type = forms.ChoiceField(
        required=False,
        choices=[('', 'Любой'), ('Эконом', 'Эконом'), ('Бизнес', 'Бизнес')],
        label="Класс"
    )
