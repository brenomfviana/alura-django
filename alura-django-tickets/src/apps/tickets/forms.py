from datetime import datetime

from django import forms
from tempus_dominus.widgets import DatePicker
from tickets.models import *
from tickets.validation import *


class TicketForms(forms.ModelForm):
    query_date = forms.DateField(
        label="Data da pesquisa", initial=datetime.today(), disabled=True
    )

    class Meta:
        model = Ticket
        fields = "__all__"
        labels = {
            "origin": "Origem",
            "destination": "Destino",
            "departure_day": "Data de Ida",
            "return_day": "Data de Volta",
            "query_date": "Data da Consulta",
            "extra_info": "Informações Extras",
            "trip_class": "Tipo de Viagem",
        }
        widgets = {
            "departure_day": DatePicker(),
            "return_day": DatePicker(),
        }

    def clean(self):
        origin = self.cleaned_data.get("origin")
        destination = self.cleaned_data.get("destination")
        departure_day = self.cleaned_data.get("departure_day")
        return_day = self.cleaned_data.get("return_day")
        query_date = self.cleaned_data.get("query_date")
        error_list = {}
        has_field_a_number(origin, "origin", error_list)
        has_field_a_number(destination, "destination", error_list)
        are_origin_destination_equal(origin, destination, error_list)
        departure_is_after_return_day(departure_day, return_day, error_list)
        departure_day_is_before_today(departure_day, query_date, error_list)
        if error_list:
            for err in error_list:
                message = error_list[err]
                self.add_error(err, message)
        return self.cleaned_data


class PersonForms(forms.ModelForm):
    class Meta:
        model = Person
        exclude = ["name"]
