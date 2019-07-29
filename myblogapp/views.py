from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage
from myblogapp.models import MsgComm,ArticleMsg
from datetime import datetime


def home(request):
    """主页视图函数"""
    msgs,newarticles = get_data()
    return render(request, "home.html", {"newarticles":newarticles,"msgs": msgs})

def sort_page(request):
    """类别页视图函数"""
    sort = request.path.split('/')[-2]
    msgs, newarticles, articleMsgs = get_data(sort = sort)
    articleMsgs = paging(request, articleMsgs)
    http_page = sort + ".html"
    return render(request, http_page, {"articles": articleMsgs, "newarticles": newarticles, "msgs": msgs})

def msgboard(request):
    """留言板视图函数"""
    if request.method == "GET":
        msgs, newarticles = get_data()
        return render(request,"msgboard.html",{"newarticles":newarticles,"msgs":msgs})
    if request.method == "POST":
        msg = MsgComm()
        message = request.POST.get('newmsg')
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        msg.file_name = "msgboard"
        msg.time = time
        msg.text = message
        msg.save()
        return redirect("/msgboard/")

def article_page(request):
    """文章视图函数"""
    file_name = request.path.split('/')[-2]
    if request.method == "GET":
        comments = get_comment(file_name)
        msgs, newarticles = get_data()
        return render(request, file_name, {"newarticles": newarticles,"comments":comments, "msgs": msgs})
    if request.method == "POST":
        sort = request.path.split('/')[-3]
        path = "/" + sort + "/" + file_name + "/"
        save_comment(request,file_name)
        return redirect(path)


def get_data(**kwargs):
    """
    从数据库获取模板需要的信息
    :param kwargs: 筛选条件
    :return: 留言，文章信息
    """
    msgs = MsgComm.objects.filter(file_name="msgboard").order_by('-time')[0:6]
    newarticles = ArticleMsg.objects.order_by('-time')[0:5]
    if kwargs:
        for key in kwargs:
            if kwargs[key] in ["skill","life","food"]:
                articleMsgs = ArticleMsg.objects.filter(sort=kwargs[key]).order_by('-time')
            else:
                articleMsgs = ArticleMsg.objects.filter(type=kwargs[key]).order_by('-time')
        return msgs,newarticles,articleMsgs
    else:
        return msgs,newarticles

def get_comment(file_name):
    """
    从数据库获取对应文章的评论
    :param file_name: 文章名称
    :return: 对应评论
    """
    comments = MsgComm.objects.filter(file_name=file_name).order_by('-time')
    return comments

def save_comment(request,file_name):
    """
    保存评论
    :param request:http请求
    :param file_name: 文章名称
    :return: none
    """
    comment = MsgComm()
    data = request.POST.get('new_comment')
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    comment.file_name = file_name
    comment.text = data
    comment.time = time
    comment.save()

def paging(request,articleMsgs):
    """
    对从数据库获取的文章列表进行分页
    :param request: http请求
    :param articleMsgs: 当前请求的所有文章列表
    :return: 当前请求页的文章列表
    """
    paginator = Paginator(articleMsgs, 5)
    if request.method == "GET":
        page = request.GET.get('page')
        try:
            articleMsgs = paginator.page(page)
        except PageNotAnInteger:
            articleMsgs = paginator.page(1)
        except InvalidPage:
            return HttpResponse("找不到页面内容")
        except EmptyPage:
            articleMsgs = paginator.page(paginator.num_pages)
    return articleMsgs
