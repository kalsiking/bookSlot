from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("calendar/<int:year>/<int:month>/", views.get_calendar, name="calendar"),
    path(
        "calendar/<int:year>/<int:month>/<int:day>",
        views.get_calendar,
        name="calendardaily",
    ),
]
