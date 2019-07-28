from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage
from myblogapp.models import Msgboard,Skill,Life,Food,Comments
from datetime import datetime
from django.db import connection



def my_connection():
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM skill UNION SELECT * FROM life UNION SELECT * FROM food ORDER BY time DESC LIMIT 5")
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]
def home(request):
    newarticles = my_connection()
    msgs = Msgboard.objects.order_by('-time')[0:3]
    return render(request, "home.html", {"newarticles":newarticles,"msgs": msgs})

def skill(request):
    newarticles = my_connection()
    msgs = Msgboard.objects.order_by('-time')[0:3]
    skills = Skill.objects.order_by('-time')
    paginator = Paginator(skills,5)
    if request.method == "GET":
        page = request.GET.get('page')
        try:
            skills = paginator.page(page)
        except PageNotAnInteger:
            skills = paginator.page(1)
        except InvalidPage:
            return HttpResponse("找不到页面内容")
        except EmptyPage:
            skills = paginator.page(paginator.num_pages)
    return render(request, "skill.html", {"articles": skills,"newarticles":newarticles,"msgs": msgs})

def skillPython(request):
    newarticles = my_connection()
    msgs = Msgboard.objects.order_by('-time')[0:3]
    skills = Skill.objects.filter(type="python").order_by('-time')
    paginator = Paginator(skills, 5)
    if request.method == "GET":
        page = request.GET.get('page')
        try:
            skills = paginator.page(page)
        except PageNotAnInteger:
            skills = paginator.page(1)
        except InvalidPage:
            return HttpResponse("找不到页面内容")
        except EmptyPage:
            skills = paginator.page(paginator.num_pages)
    return render(request, "python.html", {"articles": skills, "newarticles":newarticles,"msgs": msgs})

def skillDjango(request):
    newarticles = my_connection()
    msgs = Msgboard.objects.order_by('-time')[0:3]
    skills = Skill.objects.filter(type="django").order_by('-time')
    paginator = Paginator(skills, 5)
    if request.method == "GET":
        page = request.GET.get('page')
        try:
            skills = paginator.page(page)
        except PageNotAnInteger:
            skills = paginator.page(1)
        except InvalidPage:
            return HttpResponse("找不到页面内容")
        except EmptyPage:
            skills = paginator.page(paginator.num_pages)
    return render(request, "django.html", {"articles": skills, "newarticles":newarticles,"msgs": msgs})

def skillVue(request):
    newarticles = my_connection()
    msgs = Msgboard.objects.order_by('-time')[0:3]
    skills = Skill.objects.filter(type="vue").order_by('-time')
    paginator = Paginator(skills, 5)
    if request.method == "GET":
        page = request.GET.get('page')
        try:
            skills = paginator.page(page)
        except PageNotAnInteger:
            skills = paginator.page(1)
        except InvalidPage:
            return HttpResponse("找不到页面内容")
        except EmptyPage:
            skills = paginator.page(paginator.num_pages)
    return render(request, "vue.html", {"articles": skills,"newarticles":newarticles, "msgs": msgs})

def skillHtml(request):
    newarticles = my_connection()
    msgs = Msgboard.objects.order_by('-time')[0:3]
    skills = Skill.objects.filter(type="html").order_by('-time')
    paginator = Paginator(skills, 5)
    if request.method == "GET":
        page = request.GET.get('page')
        try:
            skills = paginator.page(page)
        except PageNotAnInteger:
            skills = paginator.page(1)
        except InvalidPage:
            return HttpResponse("找不到页面内容")
        except EmptyPage:
            skills = paginator.page(paginator.num_pages)
    return render(request, "html.html", {"articles": skills,"newarticles":newarticles, "msgs": msgs})

def skillCss(request):
    newarticles = my_connection()
    msgs = Msgboard.objects.order_by('-time')[0:3]
    skills = Skill.objects.filter(type="css").order_by('-time')
    paginator = Paginator(skills, 5)
    if request.method == "GET":
        page = request.GET.get('page')
        try:
            skills = paginator.page(page)
        except PageNotAnInteger:
            skills = paginator.page(1)
        except InvalidPage:
            return HttpResponse("找不到页面内容")
        except EmptyPage:
            skills = paginator.page(paginator.num_pages)
    return render(request, "css.html", {"articles": skills, "newarticles":newarticles,"msgs": msgs})

def skillJs(request):
    newarticles = my_connection()
    msgs = Msgboard.objects.order_by('-time')[0:3]
    skills = Skill.objects.filter(type="js").order_by('-time')
    paginator = Paginator(skills, 5)
    if request.method == "GET":
        page = request.GET.get('page')
        try:
            skills = paginator.page(page)
        except PageNotAnInteger:
            skills = paginator.page(1)
        except InvalidPage:
            return HttpResponse("找不到页面内容")
        except EmptyPage:
            skills = paginator.page(paginator.num_pages)
    return render(request, "js.html", {"articles": skills, "newarticles":newarticles,"msgs": msgs})

def life(request):
    newarticles = my_connection()
    msgs = Msgboard.objects.order_by('-time')[0:3]
    lifes = Life.objects.order_by('-time')
    paginator = Paginator(lifes, 5)
    if request.method == "GET":
        page = request.GET.get('page')
        try:
            lifes = paginator.page(page)
        except PageNotAnInteger:
            lifes = paginator.page(1)
        except InvalidPage:
            return HttpResponse("找不到页面内容")
        except EmptyPage:
            lifes = paginator.page(paginator.num_pages)
    return render(request, "life.html", {"articles":lifes,"newarticles":newarticles,"msgs": msgs})

def lifeEssay(request):
    newarticles = my_connection()
    msgs = Msgboard.objects.order_by('-time')[0:3]
    lifes = Life.objects.filter(type="essay").order_by('-time')
    paginator = Paginator(lifes, 5)
    if request.method == "GET":
        page = request.GET.get('page')
        try:
            lifes = paginator.page(page)
        except PageNotAnInteger:
            lifes = paginator.page(1)
        except InvalidPage:
            return HttpResponse("找不到页面内容")
        except EmptyPage:
            lifes = paginator.page(paginator.num_pages)
    return render(request, "essay.html", {"articles": lifes, "newarticles":newarticles,"msgs": msgs})

def lifePhoto(request):
    newarticles = my_connection()
    msgs = Msgboard.objects.order_by('-time')[0:3]
    lifes = Life.objects.filter(type="photo").order_by('-time')
    paginator = Paginator(lifes, 5)
    if request.method == "GET":
        page = request.GET.get('page')
        try:
            lifes = paginator.page(page)
        except PageNotAnInteger:
            lifes = paginator.page(1)
        except InvalidPage:
            return HttpResponse("找不到页面内容")
        except EmptyPage:
            lifes = paginator.page(paginator.num_pages)
    return render(request, "photo.html", {"articles": lifes, "newarticles":newarticles,"msgs": msgs})

def food(request):
    newarticles = my_connection()
    msgs = Msgboard.objects.order_by('-time')[0:3]
    foods = Food.objects.order_by('-time')
    paginator = Paginator(foods, 5)
    if request.method == "GET":
        page = request.GET.get('page')
        try:
            foods = paginator.page(page)
        except PageNotAnInteger:
            foods = paginator.page(1)
        except InvalidPage:
            return HttpResponse("找不到页面内容")
        except EmptyPage:
            foods = paginator.page(paginator.num_pages)
    return render(request, "food.html", {"articles":foods,"newarticles":newarticles,"msgs": msgs})

def foodTeaching(request):
    newarticles = my_connection()
    msgs = Msgboard.objects.order_by('-time')[0:3]
    foods = Food.objects.filter(type="teaching").order_by('-time')
    paginator = Paginator(foods, 5)
    if request.method == "GET":
        page = request.GET.get('page')
        try:
            foods = paginator.page(page)
        except PageNotAnInteger:
            foods = paginator.page(1)
        except InvalidPage:
            return HttpResponse("找不到页面内容")
        except EmptyPage:
            foods = paginator.page(paginator.num_pages)
    return render(request, "teaching.html", {"newarticles":newarticles,"articles": foods, "msgs": msgs})

def foodShare(request):
    newarticles = my_connection()
    msgs = Msgboard.objects.order_by('-time')[0:3]
    foods = Food.objects.filter(type="share").order_by('-time')
    paginator = Paginator(foods, 5)
    if request.method == "GET":
        page = request.GET.get('page')
        try:
            foods = paginator.page(page)
        except PageNotAnInteger:
            foods = paginator.page(1)
        except InvalidPage:
            return HttpResponse("找不到页面内容")
        except EmptyPage:
            foods = paginator.page(paginator.num_pages)
    return render(request, "share.html", {"articles": foods,"newarticles":newarticles, "msgs": msgs})

def msgboard(request):
    if request.method == "GET":
        newarticles = my_connection()
        msgs = Msgboard.objects.order_by('-time')[0:6]
        return render(request,"msgboard.html",{"newarticles":newarticles,"msgs":msgs})
    if request.method == "POST":
        msg = Msgboard()
        message = request.POST.get('newmsg')
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        msg.time = time
        msg.message = message
        msg.save()
        return redirect("/msgboard/")

def py001(request):
    if request.method == "GET":
        path = request.path
        file_name = path.split('/')[-2]
        comments = Comments.objects.filter(file_name=file_name).order_by('-time')
        newarticles = my_connection()
        msgs = Msgboard.objects.order_by('-time')[0:3]
        return render(request, "py001.html", {"newarticles": newarticles,"comments":comments, "msgs": msgs})
    if request.method == "POST":
        comment = Comments()
        path = request.path
        file_name = path.split('/')[-2]
        data = request.POST.get('new_comment')
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        comment.file_name = file_name
        comment.text = data
        comment.time = time
        comment.save()
        return redirect("/skill/py001.html/")

def py002(request):
    if request.method == "GET":
        path = request.path
        file_name = path.split('/')[-2]
        comments = Comments.objects.filter(file_name=file_name).order_by('-time')
        newarticles = my_connection()
        msgs = Msgboard.objects.order_by('-time')[0:3]
        return render(request, "py002.html", {"newarticles": newarticles, "comments": comments, "msgs": msgs})
    if request.method == "POST":
        comment = Comments()
        path = request.path
        file_name = path.split('/')[-2]
        data = request.POST.get('new_comment')
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        comment.file_name = file_name
        comment.text = data
        comment.time = time
        comment.save()
        return redirect("/skill/py002.html/")

def py003(request):
    if request.method == "GET":
        path = request.path
        file_name = path.split('/')[-2]
        comments = Comments.objects.filter(file_name=file_name).order_by('-time')
        newarticles = my_connection()
        msgs = Msgboard.objects.order_by('-time')[0:3]
        return render(request, "py003.html", {"newarticles": newarticles, "comments": comments, "msgs": msgs})
    if request.method == "POST":
        comment = Comments()
        path = request.path
        file_name = path.split('/')[-2]
        data = request.POST.get('new_comment')
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        comment.file_name = file_name
        comment.text = data
        comment.time = time
        comment.save()
        return redirect("/skill/py003.html/")

def py004(request):
    if request.method == "GET":
        path = request.path
        file_name = path.split('/')[-2]
        comments = Comments.objects.filter(file_name=file_name).order_by('-time')
        newarticles = my_connection()
        msgs = Msgboard.objects.order_by('-time')[0:3]
        return render(request, "py004.html", {"newarticles": newarticles, "comments": comments, "msgs": msgs})
    if request.method == "POST":
        comment = Comments()
        path = request.path
        file_name = path.split('/')[-2]
        data = request.POST.get('new_comment')
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        comment.file_name = file_name
        comment.text = data
        comment.time = time
        comment.save()
        return redirect("/skill/py004.html/")

def py005(request):
    if request.method == "GET":
        path = request.path
        file_name = path.split('/')[-2]
        comments = Comments.objects.filter(file_name=file_name).order_by('-time')
        newarticles = my_connection()
        msgs = Msgboard.objects.order_by('-time')[0:3]
        return render(request, "py005.html", {"newarticles": newarticles, "comments": comments, "msgs": msgs})
    if request.method == "POST":
        comment = Comments()
        path = request.path
        file_name = path.split('/')[-2]
        data = request.POST.get('new_comment')
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        comment.file_name = file_name
        comment.text = data
        comment.time = time
        comment.save()
        return redirect("/skill/py005.html/")

def py006(request):
    if request.method == "GET":
        path = request.path
        file_name = path.split('/')[-2]
        comments = Comments.objects.filter(file_name=file_name).order_by('-time')
        newarticles = my_connection()
        msgs = Msgboard.objects.order_by('-time')[0:3]
        return render(request, "py006.html", {"newarticles": newarticles, "comments": comments, "msgs": msgs})
    if request.method == "POST":
        comment = Comments()
        path = request.path
        file_name = path.split('/')[-2]
        data = request.POST.get('new_comment')
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        comment.file_name = file_name
        comment.text = data
        comment.time = time
        comment.save()
        return redirect("/skill/py006.html/")

def py007(request):
    if request.method == "GET":
        path = request.path
        file_name = path.split('/')[-2]
        comments = Comments.objects.filter(file_name=file_name).order_by('-time')
        newarticles = my_connection()
        msgs = Msgboard.objects.order_by('-time')[0:3]
        return render(request, "py007.html", {"newarticles": newarticles, "comments": comments, "msgs": msgs})
    if request.method == "POST":
        comment = Comments()
        path = request.path
        file_name = path.split('/')[-2]
        data = request.POST.get('new_comment')
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        comment.file_name = file_name
        comment.text = data
        comment.time = time
        comment.save()
        return redirect("/skill/py007.html/")

def py008(request):
    if request.method == "GET":
        path = request.path
        file_name = path.split('/')[-2]
        comments = Comments.objects.filter(file_name=file_name).order_by('-time')
        newarticles = my_connection()
        msgs = Msgboard.objects.order_by('-time')[0:3]
        return render(request, "py008.html", {"newarticles": newarticles, "comments": comments, "msgs": msgs})
    if request.method == "POST":
        comment = Comments()
        path = request.path
        file_name = path.split('/')[-2]
        data = request.POST.get('new_comment')
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        comment.file_name = file_name
        comment.text = data
        comment.time = time
        comment.save()
        return redirect("/skill/py008.html/")

def py009(request):
    if request.method == "GET":
        path = request.path
        file_name = path.split('/')[-2]
        comments = Comments.objects.filter(file_name=file_name).order_by('-time')
        newarticles = my_connection()
        msgs = Msgboard.objects.order_by('-time')[0:3]
        return render(request, "py009.html", {"newarticles": newarticles, "comments": comments, "msgs": msgs})
    if request.method == "POST":
        comment = Comments()
        path = request.path
        file_name = path.split('/')[-2]
        data = request.POST.get('new_comment')
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        comment.file_name = file_name
        comment.text = data
        comment.time = time
        comment.save()
        return redirect("/skill/py009.html/")

def py010(request):
    if request.method == "GET":
        path = request.path
        file_name = path.split('/')[-2]
        comments = Comments.objects.filter(file_name=file_name).order_by('-time')
        newarticles = my_connection()
        msgs = Msgboard.objects.order_by('-time')[0:3]
        return render(request, "py010.html", {"newarticles": newarticles, "comments": comments, "msgs": msgs})
    if request.method == "POST":
        comment = Comments()
        path = request.path
        file_name = path.split('/')[-2]
        data = request.POST.get('new_comment')
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        comment.file_name = file_name
        comment.text = data
        comment.time = time
        comment.save()
        return redirect("/skill/py010.html/")

def py011(request):
    if request.method == "GET":
        path = request.path
        file_name = path.split('/')[-2]
        comments = Comments.objects.filter(file_name=file_name).order_by('-time')
        newarticles = my_connection()
        msgs = Msgboard.objects.order_by('-time')[0:3]
        return render(request, "py011.html", {"newarticles": newarticles, "comments": comments, "msgs": msgs})
    if request.method == "POST":
        comment = Comments()
        path = request.path
        file_name = path.split('/')[-2]
        data = request.POST.get('new_comment')
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        comment.file_name = file_name
        comment.text = data
        comment.time = time
        comment.save()
        return redirect("/skill/py011.html/")

def py012(request):
    if request.method == "GET":
        path = request.path
        file_name = path.split('/')[-2]
        comments = Comments.objects.filter(file_name=file_name).order_by('-time')
        newarticles = my_connection()
        msgs = Msgboard.objects.order_by('-time')[0:3]
        return render(request, "py012.html", {"newarticles": newarticles, "comments": comments, "msgs": msgs})
    if request.method == "POST":
        comment = Comments()
        path = request.path
        file_name = path.split('/')[-2]
        data = request.POST.get('new_comment')
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        comment.file_name = file_name
        comment.text = data
        comment.time = time
        comment.save()
        return redirect("/skill/py012.html/")

def django001(request):
    if request.method == "GET":
        path = request.path
        file_name = path.split('/')[-2]
        comments = Comments.objects.filter(file_name=file_name).order_by('-time')
        newarticles = my_connection()
        msgs = Msgboard.objects.order_by('-time')[0:3]
        return render(request, "django001.html", {"newarticles": newarticles, "comments": comments, "msgs": msgs})
    if request.method == "POST":
        comment = Comments()
        path = request.path
        file_name = path.split('/')[-2]
        data = request.POST.get('new_comment')
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        comment.file_name = file_name
        comment.text = data
        comment.time = time
        comment.save()
        return redirect("/skill/django001.html/")

def vue001(request):
    if request.method == "GET":
        path = request.path
        file_name = path.split('/')[-2]
        comments = Comments.objects.filter(file_name=file_name).order_by('-time')
        newarticles = my_connection()
        msgs = Msgboard.objects.order_by('-time')[0:3]
        return render(request, "vue001.html", {"newarticles": newarticles, "comments": comments, "msgs": msgs})
    if request.method == "POST":
        comment = Comments()
        path = request.path
        file_name = path.split('/')[-2]
        data = request.POST.get('new_comment')
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        comment.file_name = file_name
        comment.text = data
        comment.time = time
        comment.save()
        return redirect("/skill/vue001.html/")

def html001(request):
    if request.method == "GET":
        path = request.path
        file_name = path.split('/')[-2]
        comments = Comments.objects.filter(file_name=file_name).order_by('-time')
        newarticles = my_connection()
        msgs = Msgboard.objects.order_by('-time')[0:3]
        return render(request, "html001.html", {"newarticles": newarticles, "comments": comments, "msgs": msgs})
    if request.method == "POST":
        comment = Comments()
        path = request.path
        file_name = path.split('/')[-2]
        data = request.POST.get('new_comment')
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        comment.file_name = file_name
        comment.text = data
        comment.time = time
        comment.save()
        return redirect("/skill/html001.html/")

def css001(request):
    if request.method == "GET":
        path = request.path
        file_name = path.split('/')[-2]
        comments = Comments.objects.filter(file_name=file_name).order_by('-time')
        newarticles = my_connection()
        msgs = Msgboard.objects.order_by('-time')[0:3]
        return render(request, "css001.html", {"newarticles": newarticles, "comments": comments, "msgs": msgs})
    if request.method == "POST":
        comment = Comments()
        path = request.path
        file_name = path.split('/')[-2]
        data = request.POST.get('new_comment')
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        comment.file_name = file_name
        comment.text = data
        comment.time = time
        comment.save()
        return redirect("/skill/css001.html/")

def js001(request):
    if request.method == "GET":
        path = request.path
        file_name = path.split('/')[-2]
        comments = Comments.objects.filter(file_name=file_name).order_by('-time')
        newarticles = my_connection()
        msgs = Msgboard.objects.order_by('-time')[0:3]
        return render(request, "js001.html", {"newarticles": newarticles, "comments": comments, "msgs": msgs})
    if request.method == "POST":
        comment = Comments()
        path = request.path
        file_name = path.split('/')[-2]
        data = request.POST.get('new_comment')
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        comment.file_name = file_name
        comment.text = data
        comment.time = time
        comment.save()
        return redirect("/skill/js001.html/")

def essay001(request):
    if request.method == "GET":
        path = request.path
        file_name = path.split('/')[-2]
        comments = Comments.objects.filter(file_name=file_name).order_by('-time')
        newarticles = my_connection()
        msgs = Msgboard.objects.order_by('-time')[0:3]
        return render(request, "essay001.html", {"newarticles": newarticles, "comments": comments, "msgs": msgs})
    if request.method == "POST":
        comment = Comments()
        path = request.path
        file_name = path.split('/')[-2]
        data = request.POST.get('new_comment')
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        comment.file_name = file_name
        comment.text = data
        comment.time = time
        comment.save()
        return redirect("/life/essay001.html/")

def photo001(request):
    if request.method == "GET":
        path = request.path
        file_name = path.split('/')[-2]
        comments = Comments.objects.filter(file_name=file_name).order_by('-time')
        newarticles = my_connection()
        msgs = Msgboard.objects.order_by('-time')[0:3]
        return render(request, "photo001.html", {"newarticles": newarticles, "comments": comments, "msgs": msgs})
    if request.method == "POST":
        comment = Comments()
        path = request.path
        file_name = path.split('/')[-2]
        data = request.POST.get('new_comment')
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        comment.file_name = file_name
        comment.text = data
        comment.time = time
        comment.save()
        return redirect("/life/photo001.html/")

def share001(request):
    if request.method == "GET":
        path = request.path
        file_name = path.split('/')[-2]
        comments = Comments.objects.filter(file_name=file_name).order_by('-time')
        newarticles = my_connection()
        msgs = Msgboard.objects.order_by('-time')[0:3]
        return render(request, "share001.html", {"newarticles": newarticles, "comments": comments, "msgs": msgs})
    if request.method == "POST":
        comment = Comments()
        path = request.path
        file_name = path.split('/')[-2]
        data = request.POST.get('new_comment')
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        comment.file_name = file_name
        comment.text = data
        comment.time = time
        comment.save()
        return redirect("/food/share001.html/")

def share002(request):
    if request.method == "GET":
        path = request.path
        file_name = path.split('/')[-2]
        comments = Comments.objects.filter(file_name=file_name).order_by('-time')
        newarticles = my_connection()
        msgs = Msgboard.objects.order_by('-time')[0:3]
        return render(request, "share002.html", {"newarticles": newarticles, "comments": comments, "msgs": msgs})
    if request.method == "POST":
        comment = Comments()
        path = request.path
        file_name = path.split('/')[-2]
        data = request.POST.get('new_comment')
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        comment.file_name = file_name
        comment.text = data
        comment.time = time
        comment.save()
        return redirect("/food/share002.html/")

def teaching001(request):
    if request.method == "GET":
        path = request.path
        file_name = path.split('/')[-2]
        comments = Comments.objects.filter(file_name=file_name).order_by('-time')
        newarticles = my_connection()
        msgs = Msgboard.objects.order_by('-time')[0:3]
        return render(request, "teaching001.html", {"newarticles": newarticles, "comments": comments, "msgs": msgs})
    if request.method == "POST":
        comment = Comments()
        path = request.path
        file_name = path.split('/')[-2]
        data = request.POST.get('new_comment')
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        comment.file_name = file_name
        comment.text = data
        comment.time = time
        comment.save()
        return redirect("/food/teaching001.html/")

def teaching002(request):
    if request.method == "GET":
        path = request.path
        file_name = path.split('/')[-2]
        comments = Comments.objects.filter(file_name=file_name).order_by('-time')
        newarticles = my_connection()
        msgs = Msgboard.objects.order_by('-time')[0:3]
        return render(request, "teaching002.html", {"newarticles": newarticles, "comments": comments, "msgs": msgs})
    if request.method == "POST":
        comment = Comments()
        path = request.path
        file_name = path.split('/')[-2]
        data = request.POST.get('new_comment')
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        comment.file_name = file_name
        comment.text = data
        comment.time = time
        comment.save()
        return redirect("/food/teaching002.html/")
