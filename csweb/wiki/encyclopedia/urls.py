from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # IMPORTANT! We have to put "search" in front of "<str:title>", cause otherwise the system will treat search as a title you want to search
    # This happens because "search" is an element/possible input of "<str:title>"
    path("search",views.search,name="search"),
    path("create",views.create,name="create"),
    path("edit",views.edit,name="edit"),
    path("editedpage",views.editedpage,name="editedpage"),
    ## we should never name something random, the same as a package
    path("rand",views.rand,name="rand"),
    path("<str:title>",views.title,name="title"), 
]
