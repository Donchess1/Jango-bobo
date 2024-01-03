from django import path
from . import views
urlpatterns = [
    path(""), views.my_view, name="details"]