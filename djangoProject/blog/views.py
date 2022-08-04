from django.http import HttpResponse
from django.shortcuts import render, redirect
from blog.models import  Article,Users
from django.core.paginator import Paginator as pr
from django.contrib import messages

# Create your views here.

def Hello(request):
    return HttpResponse('HelloWorld')
# 登录界面
def login(request):
    return render(request , 'login.html')
# 登录逻辑
def do_login(request):
    """

    获取post请求过来的用户名和密码
    获取model中的用户名和密码
    判断：

    :param request:
    :return:
    """


    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == '' or password == '':
            messages.error(request, '账号或密码不能为空!')  # 如果账号或密码为空，提示账号或密码不能为空
            redirect('login')
        else:
            user = Users.objects
            name = user.get(username=username)
            if username == name.username:
                if password == name.password:
                    request.session['username'] = username
                    messages.error(request, '登录成功!')  # 登录成功提示信息
                    return redirect('index', 1)
                else:
                    messages.error(request, '密码错误!')  # 密码错误提示信息
            else:
                messages.error(request, '账号不存在!')  # 账号不存在提示信息

def index(request):

    page = request.GET.get('page',None)
    if page == None or page == "":
        page = 1
    if not page:
        page = 1

    #将index.html中的循环变量articles作为参数传过去
    articles = Article.objects.all()
    paginator = pr(articles,3)
    page_num = paginator.num_pages
    page_article_list = paginator.page(page)

    if page_article_list.has_next():
        next_page = int(page) + 1
    else:
        next_page = int(page) + 1
    if page_article_list.has_previous():
        previous_page = int(page) -1
    else:
        previous_page = int(page)
    return render(request,'index.html',{
        'articles':page_article_list,
        'curr_page':int(page),
        'previous_page':int(previous_page),
        'next_page':int(next_page),
        'page_num':range(1,int(page_num))
    })
# def get_detail_page(request):
#     curr_article = Article.objects.all()[0]  # 表示拿到第一篇文
#     return render(request,'detail.html',{
#         'curr_article':curr_article
#     })
def get_detail_page(request,article_id):
    #
    all_article = Article.objects.all()
    p_index = 0;
    n_index = 0;
    for index,article in enumerate(all_article):
        if index ==0:
            p_index = 0
            n_index = index+1
        elif index ==len(all_article)-1:
            p_index = index-1
            n_index = index
        else:
            p_index = index-1
            n_index = index+1

        if article.article_id == article_id:
            curr_article = article
            p_article = all_article[p_index]
            n_article = all_article[n_index]
            break
    return render(request,'detail.html',{
        'curr_article':curr_article,
        'p_article':p_article,
        'n_article':n_article
    })

