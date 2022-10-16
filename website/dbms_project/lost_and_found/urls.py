from nturl2path import url2pathname
from django.urls import path
from . import views
urlpatterns = [
    path("",views.index, name="index"),
    path("form/",views.itemform,name="form"),
    path("item/",views.item,name="item"),
    path("login/",views.login,name="login"),
    path("category/",views.category,name="category"),
    path("myreq/",views.myreq,name="myreq")
]
