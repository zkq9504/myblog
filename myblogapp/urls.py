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
    path('life/essay/',views.lifeEssay),
    path('life/photo/',views.lifePhoto),
    path('food/teaching/',views.foodTeaching),
    path('food/share/',views.foodShare),
    path('skill/py001.html/',views.py001),
    path('skill/py002.html/',views.py002),
    path('skill/py003.html/',views.py003),
    path('skill/py004.html/',views.py004),
    path('skill/py005.html/',views.py005),
    path('skill/py006.html/',views.py006),
    path('skill/py007.html/',views.py007),
    path('skill/py008.html/',views.py008),
    path('skill/py009.html/',views.py009),
    path('skill/py010.html/',views.py010),
    path('skill/py011.html/',views.py011),
    path('skill/py012.html/',views.py012),
    path('skill/django001.html/',views.django001),
    path('skill/vue001.html/',views.vue001),
    path('skill/html001.html/',views.html001),
    path('skill/css001.html/',views.css001),
    path('skill/js001.html/',views.js001),
    path('life/essay001.html/',views.essay001),
    path('life/photo001.html/',views.photo001),
    path('food/share001.html/',views.share001),
    path('food/share002.html/',views.share002),
    path('food/teaching001.html/',views.teaching001),
    path('food/teaching002.html/',views.teaching002),

]