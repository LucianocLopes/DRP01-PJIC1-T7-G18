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
        day = start + timedelta(days=d) + timedelta(hours=1)
        lista_datas.append(day)
    
    return lista_datas

def days_week(date: datetime, week: int) -> list:
    start = week
    year = date.year 
    
    days = []
    for day in range(7):
        days.append(date.fromisocalendar(year, start, day+1))
    
    return days
