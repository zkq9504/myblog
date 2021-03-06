from django.shortcuts import render,redirect,get_list_or_404,get_object_or_404
from django.http import HttpResponse,Http404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage
from myblogapp.models import Article,Comment,Msg
from datetime import datetime
import markdown


def home(request):
    """主页视图函数"""
    msgs = Msg.objects.order_by('-time')[:3]
    newarticles = Article.objects.order_by('-time')[:5]
    return render(request, "home.html", {"newarticles":newarticles,"msgs": msgs})

def sort(request,sort):
    """类别页视图函数"""
    articles = Article.objects.filter(sort=sort).order_by('-time')
    if not articles:
        raise Http404("未找到对应的文章")
    msgs = Msg.objects.order_by('-time')[:3]
    newarticles = Article.objects.order_by('-time')[:5]
    articles = paging(request,articles,5)
    return render(request, "artile_list.html", {"articles": articles, "newarticles": newarticles, "msgs": msgs})

def tag(request,sort,tag):
    """标签页视图函数"""
    articles = Article.objects.filter(sort=sort,tag=tag).order_by('-time')
    if not articles:
        raise Http404("未找到对应的文章")
    msgs = Msg.objects.order_by('-time')[:3]
    newarticles = Article.objects.order_by('-time')[:5]
    articles = paging(request,articles,5)
    return render(request, "artile_list.html", {"articles": articles, "newarticles": newarticles, "msgs": msgs})

def msgboard(request):
    """留言板视图函数"""
    if request.method == "GET":
        msgs = Msg.objects.order_by('-time')
        msgs = paging(request,msgs,6)
        newarticles = Article.objects.order_by('-time')[:5]
        return render(request,"msgboard.html",{"newarticles":newarticles,"msgs":msgs})
    if request.method == "POST":
        msg = Msg()
        content = request.POST.get('newmsg')
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        msg.time = time
        msg.content = content
        print(msg.time,msg.content)
        msg.save()
        return redirect("/msgboard/")

def article(request,sort,tag,name):
    """文章视图函数"""
    article = get_object_or_404(Article, sort=sort, tag=tag, name=name)
    article.content = markdown.markdown(article.content.replace("\r\n", '  \n'), extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
    ])
    if request.method == "GET":
        comments = Comment.objects.filter(article=article).order_by('-time')
        msgs = Msg.objects.order_by('-time')[:3]
        newarticles = Article.objects.order_by('-time')[:5]
        return render(request, "article.html", {"newarticles": newarticles,"article":article,"comments":comments, "msgs": msgs})
    if request.method == "POST":
        comment = Comment(article=article)
        content = request.POST.get('new_comment')
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        comment.content = content
        comment.time = time
        comment.save()
        return redirect(request.path)

def paging(request,content_list,page_num):
    """
    分页
    :param request:http请求
    :param content_list: 需要分页的列表
    :param page_num: 每页个数
    :return:
    """
    paginator = Paginator(content_list, page_num)
    if request.method == "GET":
        page = request.GET.get('page')
        try:
            lists = paginator.page(page)
        except PageNotAnInteger:
            lists = paginator.page(1)
        except InvalidPage:
            return HttpResponse("找不到页面内容")
        except EmptyPage:
            lists = paginator.page(paginator.num_pages)
    return lists
