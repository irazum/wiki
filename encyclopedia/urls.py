from django.urls import path, re_path

from . import views


app_name = "encyclopedia"
urlpatterns = [
    re_path(r"EditPage/(?P<title>[\w\s]+)/", views.edit_page, name='EditPage'),
    path("NewPage/", views.new_page, name="NewPage"),
    path("", views.index, name="index"),
    path(r"search/", views.send_search, name="search"),
    re_path(r"(?P<title>[\w\s]+)/", views.send_entry, name="entry")

]
