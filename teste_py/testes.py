from datetime import datetime, timedelta

def number_week(dates: list)-> set:
    list = [datetime.strftime(dt, format='%W') for dt in dates]
    list_week = set(list)
    return list_week

def weeks(start: datetime, end: datetime)-> list:
    start = start
    end = end
    delta = end - start
    lista_datas = []
    for d in range(delta.days + 1):
        day = start + timedelta(days=d)
        lista_datas.append(day)
    
    return number_week(lista_datas)

def days_week(date: datetime, week: int) -> list:
    start = week
    year = date.year 
    
    days = []
    for day in range(7):
        days.append(date.fromisocalendar(year, start, day+1))
    
    return days



inicio = datetime(2024,4,5)
fim = datetime(2024,6,28)
semanas = weeks(inicio, fim)

# print(semanas)
print(sorted(list(weeks(inicio, fim))))
print(days_week(inicio, 10))