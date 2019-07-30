from django.urls import path
from . import views


urlpatterns = [
    path('',views.home),
    path('home/',views.home),
    path('msgboard/',views.msgboard),
    path('<str:sort>/',views.sort,name="sort"),
    path('<str:sort>/<str:tag>/',views.tag,name="tag"),
    path('<str:sort>/<str:tag>/<slug:name>/',views.article,name="article"),
]