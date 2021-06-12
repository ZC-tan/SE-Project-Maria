from django.shortcuts import *
from entity.models import *
from entity.form import DocForm

# Create your views here.
def home(request):
    if request.session.get('username'):
        cur_username = request.session['username']
        return render(request,"home.html",context={'username':cur_username})
    else:
        return render(request,"home.html")
    # message = 'try'
    # return render(request,"home.html",context={'username':username})

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


def modify_user_info(request):
    if request.session.get('username'):
        cur_username = request.session['username']
        cur_user = User.objects.get(name=cur_username)
        if request.method == 'POST':
            new_pass = request.post.get('new_password')
            if new_pass == request.post.get('new_password2'):
                cur_user.password = new_pass
                cur_user.save()
            else:
                return render(request, 'modify_user_info.html', {'username':cur_username,'message': '两次密码不一致'})
        else:
            return render(request, 'modify_user_info.html', {'username':cur_username})
    else:
        return redirect('login/') #如果还没登入，跳转到登入界面


def show_user_info(request):
    if request.session.get('username'):
        cur_username = request.session['username']
        cur_user = User.objects.get(name=cur_username)
        return render(request, 'show_user_info.html', {'username':cur_username,'password':cur_user.password})
    else:
        return redirect('login/')
        
def my_docslist(request):
    if request.session.get('username'):
        cur_username = request.session['username']
        my_docslist = Doc.objects.filter(creator = cur_username)
        return render(request,'mydocs.html',{'username':cur_username,'my_docslist':my_docslist})
    else:
        return redirect('login/')

def create_doc(request):
    if request.session.get('username'):
        cur_username = request.session['username']
        cur_user = User.objects.get(name=cur_username)
        if request.method == 'POST':
            form = DocForm(request.POST)
            if form.is_valid():
                newDoc = form.save(commit=False)
                newDoc.creator = cur_username
                newDoc.save()
            return redirect('/mydocs/')
        else:
            docForm = DocForm()
            return render(request,'create_doc.html',{'doc': docForm})
    else:
        return redirect('login/')
    
def edit_doc(request):
    if request.session.get('username'):
        cur_username = request.session['username']
        cur_user = User.objects.get(name=cur_username)
        if request.method == 'POST':
            form = DocForm(request.POST)
            if form.is_valid():
                newDoc = form.save(commit=False)
                newDoc.save()
            return redirect('/mydocs/')
        else:
            doc_id = request.GET.get('id')
            doc = Doc.objects.filter(id=doc_id).first()
            docForm = DocForm(instance = doc)
            return render(request,'edit_doc.html',{'title':doc.title,'doc': docForm})
    else:
        return redirect('login/')
