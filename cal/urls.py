# from django.conf.urls import url
from . import views
from django.urls import path

app_name = "cal"
urlpatterns = [
    path("index/", views.get_date, name="index"),
    path("<int:tor_id>/calendar/", views.CalendarView.as_view(), name="calendar"),
    path("event/new/", views.event, name="event_new"),
    path(
        "event/new/<int:tor_id>/<int:day>/<int:month>/<int:year>",
        views.EventNew.as_view(),
        name="event_newer",
    ),
    path("event/edit/<int:event_id>/", views.event, name="event_edit"),
    path(
        "event_details/<int:pk>/<int:tor_pk>",
        views.EventDetail.as_view(),
        name="event_detail",
    ),
    path(
        "event_delete/<int:pk>/<int:tor_pk>",
        views.EventDelete.as_view(),
        name="event_delete",
    ),
]
