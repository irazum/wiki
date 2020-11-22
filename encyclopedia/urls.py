from django.urls import path

from . import views


app_name = "encyclopedia"
urlpatterns = [
    path("", views.index, name="index"),
    path("<slug:title>/", views.send_entry, name="entry"),
    path(r"^search/$", views.send_search, name="search")
]
