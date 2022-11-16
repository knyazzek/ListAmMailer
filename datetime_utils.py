from datetime import datetime

MONTHS_MAPPING = {
    'Январь': 1,
    'Февраль': 2,
    'Март': 3,
    'Апрель': 4,
    'Май': 5,
    'Июнь': 6,
    'Июль': 7,
    'Август': 8,
    'Сентябрь': 9,
    'Октябрь': 10,
    'Ноябрь': 11,
    'Декабрь': 12
}


# Example: Вторник, Ноябрь 15, 2022 22:23
def convert_to_datatime(datetime_str):
    _, date_str, year_time_str = datetime_str.split(", ")
    month_str, day_str = date_str.split(" ")

    month_index = MONTHS_MAPPING.get(month_str)

    final_datatime_str = f"{day_str} {month_index} {year_time_str}"
    return datetime.strptime(final_datatime_str, '%d %m %Y %H:%M')
