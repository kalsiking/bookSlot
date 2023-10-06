import calendar
from datetime import datetime, timedelta

from django.http import HttpResponse
from django.shortcuts import redirect, render

from .models import Schedules


def index(request):
    now = datetime.now()
    return redirect("schedules:calendardaily", now.year, now.month, now.day)


def about(request):
    return HttpResponse("this is not done go away")


def get_calendar(request, year, month, day=None):
    if day:
        is_monthly = False
    else:
        is_monthly = True

    schedules = []
    kwargs = {
        "StartTime__year": year,
        "StartTime__month": month,
    }
    if day:
        kwargs["StartTime__day"] = day
    schedules = []
    for schedule in Schedules.objects.filter(**kwargs):

        result = {
            "StartTime": schedule.StartTime,
            "EndTime": schedule.StartTime
            + timedelta(minutes=schedule.ServiceTable.LengthInMinutes),
            "Customer": schedule.Customer,
            "ServiceTable": schedule.ServiceTable,
        }
        schedules.append(result)
    dates = []

    calendar.setfirstweekday(6)
    calen = calendar.month(year, month, w=2)
    lines = calen.strip().split("\n")[2:]
    calen = 0
    for line in lines:
        days = line.split()
        if calen == 0 and len(days) < 7:
            days = [None] * (7 - len(days)) + days
        dates.append(days)
        calen += 1

    next_year = year
    prev_year = year
    next_month = month + 1
    if next_month > 12:
        next_month = 1
        next_year = next_year + 1
    prev_month = month - 1
    if prev_month < 1:
        prev_month = 12
        prev_year = prev_year - 1

    month_num = month
    if month == 1:
        month = "January"
    elif month == 2:
        month = "Feburary"
    elif month == 3:
        month = "March"
    elif month == 4:
        month = "April"
    elif month == 5:
        month = "May"
    elif month == 6:
        month = "June"
    elif month == 7:
        month = "July"
    elif month == 8:
        month = "August"
    elif month == 9:
        month = "September"
    elif month == 10:
        month = "October"
    elif month == 11:
        month = "November"
    elif month == 12:
        month = "December"

    if is_monthly:
        if len(schedules) < 40:
            color = "green-50"
        elif len(schedules) < 75:
            color = "green-200"
        elif len(schedules) < 100:
            color = "green-400"
        elif len(schedules) < 150:
            color = "yellow-300"
        elif len(schedules) < 200:
            color = "yellow-600"
        elif len(schedules) < 240:
            color = "red-500"
        elif len(schedules) < 280:
            color = "red-800"
        elif len(schedules) < 300:
            color = "red-900"
        elif len(schedules) < 340:
            color = "pink-900"
        else:
            color = "purple-900"
    else:
        if len(schedules) < 2:
            color = "green-50"
        elif len(schedules) < 3:
            color = "green-200"
        elif len(schedules) < 5:
            color = "green-400"
        elif len(schedules) < 7:
            color = "yellow-300"
        elif len(schedules) < 9:
            color = "yellow-600"
        elif len(schedules) < 11:
            color = "red-500"
        elif len(schedules) < 14:
            color = "red-800"
        elif len(schedules) < 17:
            color = "red-900"
        elif len(schedules) < 20:
            color = "pink-900"
        elif len(schedules) < 25:
            color = "purple-900"
        else:
            color = "gray-900"

    context = {
        "schedules": schedules,
        "dates": dates,
        "month": month,
        "year": year,
        "day": str(day) if day else None,
        "is_monthly": is_monthly,
        "month_num": month_num,
        "next_month": next_month,
        "prev_month": prev_month,
        "next_year": next_year,
        "prev_year": prev_year,
        "color": color,
    }

    print(day)
    print(schedules)
    return render(request, "schedules/index.html", context)
