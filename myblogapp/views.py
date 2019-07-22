from django.shortcuts import render,redirect
from myblogapp.models import Msgboard
from datetime import datetime

def home(request):
    msgs = Msgboard.objects.order_by('-time')[0:3]
    return render(request, "home.html", {"msgs": msgs})

def skill(request):
    msgs = Msgboard.objects.order_by('-time')[0:3]
    return render(request, "skill.html", {"msgs": msgs})

def life(request):
    msgs = Msgboard.objects.order_by('-time')[0:3]
    return render(request, "life.html", {"msgs": msgs})

def food(request):
    msgs = Msgboard.objects.order_by('-time')[0:3]
    return render(request, "food.html", {"msgs": msgs})

def message(request):
    if request.method == "GET":
        msgs = Msgboard.objects.order_by('-time')[0:5]
        return render(request,"message.html",{"msgs":msgs})
    if request.method == "POST":
        msg = Msgboard()
        message = request.POST.get('newmsg')
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        msg.time = time
        msg.message = message
        msg.save()
        return redirect("/message/")