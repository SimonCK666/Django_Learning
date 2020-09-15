from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#渲染登录页面
def index_view(request):
    return render(request, 'stu/login.html')

# 处理登录功能
def login_view(request):
    # 接受表单请求参数
    uname = request.GET.get('uname', '')
    pwd = request.GET.get('pwd', '')

    # 判断
    if uname == 'Simon' and pwd == '123':
        return HttpResponse('Success!!')

    return HttpResponse('Failed!!!')