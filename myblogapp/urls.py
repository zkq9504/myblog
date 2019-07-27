from django.urls import path
from . import views


urlpatterns = [
    path('',views.home),
    path('home/',views.home),
    path('skill/',views.skill),
    path('life/',views.life),
    path('food/',views.food),
    path('msgboard/',views.msgboard),
    path('skill/python/',views.skillPython),
    path('skill/django/',views.skillDjango),
    path('skill/vue/', views.skillVue),
    path('skill/html/',views.skillHtml),
    path('skill/css/',views.skillCss),
    path('skill/js/',views.skillJs),
]