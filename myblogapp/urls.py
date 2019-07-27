from django.urls import path
from . import views


urlpatterns = [
    path('',views.home),
    path('home/',views.home),
    path('skill/',views.skill),
    path('life/',views.life),
    path('food/',views.food),
    path('msgboard/',views.msgboard),
    path('skill/py001.html/',views.skillArticle),
]