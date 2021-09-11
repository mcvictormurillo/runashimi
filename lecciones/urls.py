from lecciones.views import *
from django.urls import path, re_path
from app import views

urlpatterns = [
    path("curso/", curso, name="curso" ),
    path("conf/", conf, name="conf" ),
    path("leccion1/", leccion1, name="leccion1"),
    path("leccion1.1/", leccion1_1, name="leccion1_1"),
    path("leccion1.2/", leccion1_2, name="leccion1_2"),
    path("leccion1.3/", leccion1_3, name="leccion1_3"),

    
    path("leccion2/", leccion2, name="leccion2"),
    path("leccion3/", leccion3, name="leccion3"),
    path("leccion4/", leccion4, name="leccion4"),
    path("leccion5/", leccion5, name="leccion5"),
    path("leccion6/", leccion6, name="leccion6"),
    path("leccion7/", leccion7, name="leccion7"),
]