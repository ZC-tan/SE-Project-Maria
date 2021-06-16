from django.core.checks import messages
from django.db.models.base import Model
from django.db.models.query import QuerySet
from django.shortcuts import *
from entity.models import *
from entity.form import DocForm


#███╗   ███╗██╗   ██╗██╗███╗   ██╗███████╗ ██████╗ 
#████╗ ████║╚██╗ ██╔╝██║████╗  ██║██╔════╝██╔═══██╗
#██╔████╔██║ ╚████╔╝ ██║██╔██╗ ██║█████╗  ██║   ██║
#██║╚██╔╝██║  ╚██╔╝  ██║██║╚██╗██║██╔══╝  ██║   ██║
#██║ ╚═╝ ██║   ██║   ██║██║ ╚████║██║     ╚██████╔╝
#╚═╝     ╚═╝   ╚═╝   ╚═╝╚═╝  ╚═══╝╚═╝      ╚═════╝ 
                                                  
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
        return redirect('/login/')

#修改用户信息（密码）
def modify_user_info(request):
    if request.session.get('username'): #如果登入了
        cur_username = request.session['username']
        cur_user = User.objects.get(name=cur_username) #用名字查询用户
        if request.method == 'POST':
            new_pass = request.POST.get('new_password') #新密码
            if new_pass == request.POST.get('new_password2'): #确认新密码
                cur_user.password = new_pass
                cur_user.save()
                return redirect('/show_user_info')
            else:
                return render(request, 'modify_user_info.html', {'username':cur_username,'message': '两次密码不一致'})
        else:
            return render(request, 'modify_user_info.html', {'username':cur_username})
    else:#如果还没登入，跳转到登入界面
        return redirect('/login/') 


                                                                                            

#███╗   ███╗██╗   ██╗██████╗  ██████╗  ██████╗
#████╗ ████║╚██╗ ██╔╝██╔══██╗██╔═══██╗██╔════╝
#██╔████╔██║ ╚████╔╝ ██║  ██║██║   ██║██║     
#██║╚██╔╝██║  ╚██╔╝  ██║  ██║██║   ██║██║     
#██║ ╚═╝ ██║   ██║   ██████╔╝╚██████╔╝╚██████╗
#╚═╝     ╚═╝   ╚═╝   ╚═════╝  ╚═════╝  ╚═════╝
                                                 
#显示我创建的文档
def my_docslist(request):
    if request.session.get('username'):
        cur_username = request.session['username']
        my_docslist = Doc.objects.filter(is_group_doc=False).filter(creator = cur_username).filter(is_recycled = False) #用用户名字对应 creator 名字，查找文档
        return render(request,'mydocs.html',{'username':cur_username,'my_docslist':my_docslist}) #返回所有找到的文档
    else:
        return redirect('/login/')

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
        return redirect('/login/')

#修改文档
def edit_doc(request):
    if request.session.get('username'):
        cur_username = request.session['username']
        cur_user = User.objects.get(name=cur_username)
        doc_id = request.GET.get('id') #根绝GET 请求传进来的id，找到对应的文档，并显示
        doc = Doc.objects.filter(id=doc_id).first()
        if request.method == 'POST':   
            form = DocForm(request.POST, instance=doc) #如果POST请求，就代表用户按了submit，则用POST创建DocForm(一种 ModelForm)的表单
            if form.is_valid():
                newDoc = form.save(commit=False)
                newDoc.save()
            return redirect('/mydocs/')
        else:
            docForm = DocForm(instance = doc)
            return render(request,'edit_doc.html',{'title':doc.title,'doc': docForm})
    else:
        return redirect('/login/')

#把文档放进回收站（修改is_recycled来标注）
def recycle_doc(request):
    if request.session.get('username'):
        cur_username = request.session['username']
        doc_id = request.GET.get('id')
        doc = Doc.objects.filter(id=doc_id).first()
        doc.is_recycled = True
        doc.save()
        return redirect('/mydocs/')
    else:
        return redirect('/login/')


# ██████╗ ██████╗  ██████╗ ██╗   ██╗██████╗ 
#██╔════╝ ██╔══██╗██╔═══██╗██║   ██║██╔══██╗
#██║  ███╗██████╔╝██║   ██║██║   ██║██████╔╝
#██║   ██║██╔══██╗██║   ██║██║   ██║██╔═══╝ 
#╚██████╔╝██║  ██║╚██████╔╝╚██████╔╝██║     
# ╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝     
                                           
#发送邀请别人进group
def invite_to_group(request):
    if request.session.get('username'):
        cur_username = request.session['username']
        cur_user = User.objects.get(name=cur_username)
        if request.method == 'POST': #Post请求，输入了要邀请人的名字，按了send
            #填充邀请信息
            invitation = InviteMessage()
            invitation.sender_name = cur_username
            #先查询欲邀请的人是否存在
            receiverName = request.POST.get('receiver')
            if User.objects.filter(name = receiverName).exists():
                receiver = User.objects.filter(name = receiverName).first()
                # invitation.receiver_name = receiverName
            else:
                return render(request,'invite_to_group.html',{'message':"此用户不存在"})
            #查询发送者是不是在这个group里/group存不存在
            group_id = request.POST.get('group')
            if Group.objects.filter(id = group_id).exists():
                group = Group.objects.get(id = group_id)
                if GroupMember.objects.filter(user_name = cur_username).exists():
                    invitation.group_id = group_id
                else:
                    return render(request,'invite_to_group.html',{'message':"你不在这样的团队"})
            else:
                return render(request,'invite_to_group.html',{'message':"此团队不存在"})
            #查询欲邀请的人是否已经在group里
            if GroupMember.objects.filter(user_name = receiverName).exists():
                return render(request,'invite_to_group.html',{'message':"此用户已存在这个团队"})
            else:
                invitation.receiver_name = receiverName
            #查询这个文档是否存在刚才输入的group里
            # docId = request.POST.get('doc_Id')
            # if Doc.objects.filter(is_group_doc = True).filter(doc_group_id = group_id).exists():
            #     invitation.document_id = docId
            # else:
            #     return render(request,'invite_to_group.html',{'messages':"你的团队中没有这个的文档"})
            invitation.content = invitation.sender_name + " have inited you to join Group: " +group.name
            invitation.save()
            return redirect('/')
        else:
            return render(request,'invite_to_group.html')
            #get 请求，刚进邀请人界面
    else:
        return redirect('/login/')


# 查看自己目前有什么组
def mygroup(request):
    # 如果用户已经登录了
    if request.session.get('username'):
        cur_username = request.session['username']
        cur_user = User.objects.get(name = cur_username)
        my_groups = GroupMember.objects.filter(user_name = cur_username).all()
        my_grouplist = Group.objects.none()
        for group in my_groups.iterator():
            my_grouplist |= Group.objects.filter(id = group.group_id)
        # 返回有“我”的团队名
        return render(request, 'mygroup.html', {'username': cur_username, 'my_grouplist': my_grouplist})
    else:
        return redirect('/login/')

# 已登录的用户创建group
def creategroup(request):
    # 如果用户已经登录了
    if request.session.get('username'):
        cur_username = request.session['username']
        cur_user = User.objects.get(name=cur_username)
        if request.method == 'POST':
            new_group = Group()
            new_group.leader_name = cur_username
            new_group.groupname = request.POST.get('groupname')
            new_group.save()

            newGroupMember = GroupMember()
            newGroupMember.group_id = new_group.id
            newGroupMember.user_name = cur_username
            newGroupMember.save()
            #POST 请求创建团队成功，返回到自己的group列表
            return redirect(mygroup)
        else: #创建团队的页面
            return render(request,'newgroup.html')
    else:
        return redirect('/login/')

#查看团队详情
def show_group_info(request):
    if request.session.get('username'):
        cur_username = request.session['username']
        cur_user = User.objects.get(name=cur_username)
        #get 请求得到团队id，用这个id显示团队信息
        group_id = request.GET.get('group_id')
        group = Group.objects.filter(id = group_id).first()
        return render(request,'show_group_info.html',{'group':group})
    else:
        return redirect('/login/')


#查看团队里的文档
def show_group_doc(request):
    if request.session.get('username'):
        cur_username = request.session['username']
        cur_user = User.objects.get(name=cur_username)
        #get 请求得到团队id，用这个id显示团队文档
        group_id = request.GET.get('group_id')
        group = Group.objects.get(id = group_id)   #TODO 修改权限
        #队长和队员看到的要有区别。。。
        if group.leader_name == cur_username:
            my_docslist = Doc.objects.filter(is_group_doc=True).filter(doc_group_id = group_id)
            return render(request,'mydocs.html',{'group':group,'my_docslist':my_docslist})
        else:
            my_docslist = Doc.objects.filter(is_group_doc=True).filter(doc_group_id = group_id).filter(others_modify_right = True)
            return render(request,'mydocs.html',{'group':group,'my_docslist':my_docslist})
    else:
        return redirect('/login/')

#创建团队文档
def create_group_doc(request):
    if request.session.get('username'):
        cur_username = request.session['username']
        cur_user = User.objects.get(name=cur_username)
        group_id = request.GET.get('group_id')
        group = Group.objects.get(id = group_id)
        cur_group_member = GroupMember.objects.filter(group_id = group_id).filter(user_name = cur_username)
        #检查权限
        if group.leader_name == cur_username or cur_group_member.others_create_right == True:
            if request.method == 'POST':
                form = DocForm(request.POST) #如果POST请求，就代表用户按了submit，则用POST创建DocForm(一种 ModelForm)的表单
                if form.is_valid():
                    newDoc = form.save(commit=False) #用DocForm表单存储 Doc 文档类信息
                    newDoc.creator = cur_username
                    newDoc.is_group_doc = True
                    newDoc.group = group_id
                    newDoc.save()
                    return redirect('/show_group_doc/')
                else:
                    docForm = DocForm()
                    return render(request,'create_doc.html',{'doc': docForm})
        else:
            request.session['message'] = "您没有权限创建文档"
            return redirect('/show_group_doc/')
    else:
        return redirect('/login/')

#██╗███╗   ██╗██╗   ██╗██╗████████╗███████╗███████╗
#██║████╗  ██║██║   ██║██║╚══██╔══╝██╔════╝██╔════╝
#██║██╔██╗ ██║██║   ██║██║   ██║   █████╗  ███████╗
#██║██║╚██╗██║╚██╗ ██╔╝██║   ██║   ██╔══╝  ╚════██║
#██║██║ ╚████║ ╚████╔╝ ██║   ██║   ███████╗███████║
#╚═╝╚═╝  ╚═══╝  ╚═══╝  ╚═╝   ╚═╝   ╚══════╝╚══════╝

#查看我收到的邀请
def myinvitations(request):
    if request.session.get('username'):
        cur_username = request.session['username']
        cur_user = User.objects.get(name=cur_username)
        my_invitation = InviteMessage.objects.filter(receiver_name = cur_username).all()
        return render(request, 'myinvitations.html', {'username': cur_username, 'my_invitation': my_invitation})
    else:
        return redirect('/login/')


#接受邀请
def accept_invites(request):
    if request.session.get('username'):
        cur_username = request.session['username']
        cur_user = User.objects.get(name=cur_username)
        #Get请求获取邀请函id
        inv_id = request.GET.get('inv_id')
        #数据库中找到邀请函
        invitation = InviteMessage.objects.get(id=inv_id)
        #根据邀请函，加人入团队
        if Group.objects.filter(id=invitation.group_id).exists():
            group = Group.objects.get(id=invitation.group_id)
            newGroupMember = GroupMember()
            newGroupMember.group_id = group.id
            newGroupMember.user_name = cur_username
            newGroupMember.save()
            #删除邀请
            invitation.delete()
            redirect('/mygroup/')
        else:
            redirect('/myinvitations/')
    else:
        return redirect('/login/')

#拒绝邀请
def accept_invites(request):
    if request.session.get('username'):
        cur_username = request.session['username']
        cur_user = User.objects.get(name=cur_username)
        #Get请求获取邀请函id
        inv_id = request.GET.get('inv_id')
        #数据库中找到邀请函
        invitation = InviteMessage.objects.get(id=inv_id)
        invitation.delete()
        redirect('/mygroup/')
    else:
        return redirect('/login/')



# 后端：
# recycle 个人文档,查看，删除被 recycle 个人文档,
# favourite
#  
# 组长设置权限
# 创建，查看，修改团队文档
# 
# 查看特定组里有其他什么组员
# 踢成员（会发消息）

# 退出团队（给组长发消息？？？）

# 评论？

#检查 register/login 密码判断