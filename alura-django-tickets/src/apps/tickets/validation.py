def are_origin_destination_equal(origin, destination, error_list):
    if origin == destination:
        error_list["destination"] = "Origem e destino não podem ser iguais!"


def has_field_a_number(field, field_name, error_list):
    if any(char.isdigit() for char in field):
        error_list[field_name] = "Não inclua números neste campo!"


def departure_is_after_return_day(departure_day, return_day, error_list):
    if departure_day > return_day:
        error_list["return_day"] = "Data de volta não pode ser antes da data de ida!"


def departure_day_is_before_today(departure_day, query_date, error_list):
    if query_date > departure_day:
        error_list["departure_day"] = "Data de ida não pode ser  antes de hoje!"
