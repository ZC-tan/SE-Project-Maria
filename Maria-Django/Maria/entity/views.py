from django.shortcuts import *
from entity.models import *
from entity.form import DocForm

# Create your views here.
def home(request):
    #如果已经登陆，回到主界面时，要可以查看文档，信息等
    if request.session.get('username'):
        cur_username = request.session['username']
        return render(request,"home.html",context={'username':cur_username})
    else: #否则回到，显示登入注册的主界面
        return render(request,"home.html")

def register(request):
    if request.method == 'POST':
        new_username = request.POST.get('username')
        new_password1 = request.POST.get('password1')
        new_password2 = request.POST.get('password2')
        if User.objects.filter(name=new_username).count() >= 1:
            return render(request, 'register.html', {'message': '用户名重复'})
        elif new_password2 != new_password1:
            return render(request, 'register.html', {'message': '两次密码不一致'})
        else:
            new_user = User()
            new_user.name = new_username
            new_user.password = new_password1
            new_user.save()
            return render(request, 'home.html', {'message': '注册成功！'})
    else:
        return render(request, 'register.html', {})


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if User.objects.filter(name=username).exists():
            user = User.objects.get(name=username)
            if user.password == password:
                request.session['username'] = username
                return render(request, 'home.html', {'username': username, 'message': '登陆成功'})
            else:
                return render(request, 'login.html', {'message': '密码错误'})
        else:
            return render(request, 'login.html', {'message': '用户不存在，请先注册'})
    else:
        return render(request, 'login.html', {'message': '请登录'})


def logout(request):
    request.session.flush()
    return render(request, 'home.html', {'message': '注销成功'})

#查看用户信息
def show_user_info(request): #如果登入了
    if request.session.get('username'):
        cur_username = request.session['username']
        cur_user = User.objects.get(name=cur_username) #用名字查询用户，显示用户信息（密码，用户名）
        return render(request, 'show_user_info.html', {'username':cur_username,'password':cur_user.password})
    else: #如果还没登入，跳转到登入界面（下面多数也是这样的。。。）
        return redirect('login/')

#修改用户信息（密码）
def modify_user_info(request):
    if request.session.get('username'): #如果登入了
        cur_username = request.session['username']
        cur_user = User.objects.get(name=cur_username) #用名字查询用户
        if request.method == 'POST':
            new_pass = request.post.get('new_password') #新密码
            if new_pass == request.post.get('new_password2'): #确认新密码
                cur_user.password = new_pass
                cur_user.save()
            else:
                return render(request, 'modify_user_info.html', {'username':cur_username,'message': '两次密码不一致'})
        else:
            return render(request, 'modify_user_info.html', {'username':cur_username})
    else:#如果还没登入，跳转到登入界面
        return redirect('login/') 

#显示我创建的文档
def my_docslist(request):
    if request.session.get('username'):
        cur_username = request.session['username']
        my_docslist = Doc.objects.filter(creator = cur_username) #用用户名字对应 creator 名字，查找文档
        return render(request,'mydocs.html',{'username':cur_username,'my_docslist':my_docslist}) #返回所有找到的文档
    else:
        return redirect('login/')

#创建文档
def create_doc(request):
    if request.session.get('username'):
        cur_username = request.session['username']
        cur_user = User.objects.get(name=cur_username)
        if request.method == 'POST':
            form = DocForm(request.POST) #如果POST请求，就代表用户按了submit，则用POST创建DocForm(一种 ModelForm)的表单
            if form.is_valid():
                newDoc = form.save(commit=False) #用DocForm表单存储 Doc 文档类信息
                newDoc.creator = cur_username
                newDoc.save()
            return redirect('/mydocs/')
        else:
            docForm = DocForm()
            return render(request,'create_doc.html',{'doc': docForm})
    else:
        return redirect('login/')

#修改文档
def edit_doc(request):
    if request.session.get('username'):
        cur_username = request.session['username']
        cur_user = User.objects.get(name=cur_username)
        if request.method == 'POST':
            form = DocForm(request.POST) #如果POST请求，就代表用户按了submit，则用POST创建DocForm(一种 ModelForm)的表单
            if form.is_valid():
                newDoc = form.save(commit=False)
                newDoc.save()
            return redirect('/mydocs/')
        else:
            doc_id = request.GET.get('id') #根绝GET 请求传进来的id，找到对应的文档，并显示
            doc = Doc.objects.filter(id=doc_id).first()
            docForm = DocForm(instance = doc)
            return render(request,'edit_doc.html',{'title':doc.title,'doc': docForm})
    else:
        return redirect('login/')
