from django.shortcuts import render,redirect
from myblogapp.models import Msgboard,Skill,Life,Food,Comments
from datetime import datetime

def home(request):
    msgs = Msgboard.objects.order_by('-time')[0:3]
    return render(request, "home.html", {"msgs": msgs})

def skill(request):
    msgs = Msgboard.objects.order_by('-time')[0:3]
    skills = Skill.objects.order_by('-time')[0:5]
    return render(request, "skill.html", {"articles": skills,"msgs": msgs})

def skillPython(request):
    msgs = Msgboard.objects.order_by('-time')[0:3]
    skills = Skill.objects.filter(type="python").order_by('-time')[0:5]
    return render(request, "python.html", {"articles": skills, "msgs": msgs})

def skillDjango(request):
    msgs = Msgboard.objects.order_by('-time')[0:3]
    skills = Skill.objects.filter(type="django").order_by('-time')[0:5]
    return render(request, "django.html", {"articles": skills, "msgs": msgs})

def skillVue(request):
    msgs = Msgboard.objects.order_by('-time')[0:3]
    skills = Skill.objects.filter(type="vue").order_by('-time')[0:5]
    return render(request, "vue.html", {"articles": skills, "msgs": msgs})

def skillHtml(request):
    msgs = Msgboard.objects.order_by('-time')[0:3]
    skills = Skill.objects.filter(type="html").order_by('-time')[0:5]
    return render(request, "html.html", {"articles": skills, "msgs": msgs})

def skillCss(request):
    msgs = Msgboard.objects.order_by('-time')[0:3]
    skills = Skill.objects.filter(type="css").order_by('-time')[0:5]
    return render(request, "css.html", {"articles": skills, "msgs": msgs})

def skillJs(request):
    msgs = Msgboard.objects.order_by('-time')[0:3]
    skills = Skill.objects.filter(type="javascript").order_by('-time')[0:5]
    return render(request, "js.html", {"articles": skills, "msgs": msgs})

def life(request):
    msgs = Msgboard.objects.order_by('-time')[0:3]
    return render(request, "life.html", {"msgs": msgs})

def food(request):
    msgs = Msgboard.objects.order_by('-time')[0:3]
    return render(request, "food.html", {"msgs": msgs})

def msgboard(request):
    if request.method == "GET":
        msgs = Msgboard.objects.order_by('-time')[0:5]
        return render(request,"msgboard.html",{"msgs":msgs})
    if request.method == "POST":
        msg = Msgboard()
        message = request.POST.get('newmsg')
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        msg.time = time
        msg.message = message
        msg.save()
        return redirect("/msgboard/")
