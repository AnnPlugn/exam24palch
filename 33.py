import datetime

def find_day_of_week(day, month, year):
    input_date = datetime.date(year, month, day)
    days_of_week = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
    return days_of_week[input_date.weekday()]

date1 = (13, 8, 2005)
date2 = (12, 4, 1961)

print(f"День недели для {date1[0]}.{date1[1]}.{date1[2]}: {find_day_of_week(*date1)}")
print(f"День недели для {date2[0]}.{date2[1]}.{date2[2]}: {find_day_of_week(*date2)}")
"""".Разработать программу вычисления дня недели для произвольной даты, например, 9
мая 1945 года, 12 апреля 1961 года. 
 """""