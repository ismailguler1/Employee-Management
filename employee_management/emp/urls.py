from django.urls import path
from . import views



urlpatterns = [
    path("",              views.allemployees, name="allemployees"),
    path("allemployees/", views.allemployees, name="allemployees"),
    path("singleemployee/<int:empid>/", views.singleemployee,    name="singleemployee"),
    path("addemployee/",                views.addemployee,       name="addemployee"),
    path("editemployee/<int:empid>/",   views.editemployee,    name="editemployee"),
    path("doeditemployee/<int:empid>/",   views.doeditemployee,    name="doeditemployee"),
    path("deleteemployee/<int:empid>/", views.deleteemployee,    name="deleteemployee"),
]










