from django.core.checks import messages
from django.db.models.query import QuerySet
from django.shortcuts import *
from django.views import View
from django.https import HttpResponse, JsonResponse
import json

from rest_framework.viewsets import ModelViewSet

from entity.models import *
from entity.form import DocForm
from .models import GroupMember
from .models import Group
from .serializers import GroupMemberSerializer


# Create your views here.
def home(request):
    # 如果已经登陆，回到主界面时，要可以查看文档，信息等
    if request.session.get('username'):
        cur_username = request.session['username']
        return render(request, "home.html", context={'username': cur_username})
    else:  # 否则回到，显示登入注册的主界面
        return render(request, "home.html")


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


# 查看用户信息
def show_user_info(request):  # 如果登入了
    if request.session.get('username'):
        cur_username = request.session['username']
        cur_user = User.objects.get(name=cur_username)  # 用名字查询用户，显示用户信息（密码，用户名）
        return render(request, 'show_user_info.html', {'username': cur_username, 'password': cur_user.password})
    else:  # 如果还没登入，跳转到登入界面（下面多数也是这样的。。。）
        return redirect('/login/')


# 修改用户信息（密码）
def modify_user_info(request):
    if request.session.get('username'):  # 如果登入了
        cur_username = request.session['username']
        cur_user = User.objects.get(name=cur_username)  # 用名字查询用户
        if request.method == 'POST':
            new_pass = request.POST.get('new_password')  # 新密码
            if new_pass == request.POST.get('new_password2'):  # 确认新密码
                cur_user.password = new_pass
                cur_user.save()
                return redirect('/show_user_info')
            else:
                return render(request, 'modify_user_info.html', {'username': cur_username, 'message': '两次密码不一致'})
        else:
            return render(request, 'modify_user_info.html', {'username': cur_username})
    else:  # 如果还没登入，跳转到登入界面
        return redirect('/login/')

    # 显示我创建的文档


def my_docslist(request):
    if request.session.get('username'):
        cur_username = request.session['username']
        my_docslist = Doc.objects.filter(creator=cur_username).filter(is_recycled=False)  # 用用户名字对应 creator 名字，查找文档
        return render(request, 'mydocs.html', {'username': cur_username, 'my_docslist': my_docslist})  # 返回所有找到的文档
    else:
        return redirect('/login/')


# 创建文档
def create_doc(request):
    if request.session.get('username'):
        cur_username = request.session['username']
        cur_user = User.objects.get(name=cur_username)
        if request.method == 'POST':
            form = DocForm(request.POST)  # 如果POST请求，就代表用户按了submit，则用POST创建DocForm(一种 ModelForm)的表单
            if form.is_valid():
                newDoc = form.save(commit=False)  # 用DocForm表单存储 Doc 文档类信息
                newDoc.creator = cur_username
                newDoc.save()
            return redirect('/mydocs/')
        else:
            docForm = DocForm()
            return render(request, 'create_doc.html', {'doc': docForm})
    else:
        return redirect('/login/')


# 修改文档
def edit_doc(request):
    if request.session.get('username'):
        cur_username = request.session['username']
        cur_user = User.objects.get(name=cur_username)
        if request.method == 'POST':
            form = DocForm(request.POST)  # 如果POST请求，就代表用户按了submit，则用POST创建DocForm(一种 ModelForm)的表单
            if form.is_valid():
                newDoc = form.save(commit=False)
                newDoc.save()
            return redirect('/mydocs/')
        else:
            doc_id = request.GET.get('id')  # 根绝GET 请求传进来的id，找到对应的文档，并显示
            doc = Doc.objects.filter(id=doc_id).first()
            docForm = DocForm(instance=doc)
            return render(request, 'edit_doc.html', {'title': doc.title, 'doc': docForm})
    else:
        return redirect('/login/')


# 发送邀请别人进group
def invite_to_group(request):
    if request.session.get('username'):
        cur_username = request.session['username']
        cur_user = User.objects.get(name=cur_username)
        if request.method == 'POST':  # Post请求，输入了要邀请人的名字，按了send
            # 填充邀请信息
            invitation = InviteMessage()
            invitation.sender_name = cur_username
            # 先查询欲邀请的人是否存在
            receiverName = request.POST.get('receiver')
            if User.objects.filter(name=receiverName).exists():
                receiver = User.objects.filter(name=receiverName).first()
                # invitation.receiver_name = receiverName
            else:
                return render(request, 'invite_to_group.html', {'message': "此用户不存在"})
            # 查询发送者是不是在这个group里/group存不存在
            group_id = request.POST.get('group')
            if Group.objects.filter(id=group_id).exists():
                if GroupMember.objects.filter(user_id=cur_user.id).exists():
                    invitation.group_id = group_id
                else:
                    return render(request, 'invite_to_group.html', {'message': "你不在这样的团队"})
            else:
                return render(request, 'invite_to_group.html', {'message': "此团队不存在"})
            # 查询欲邀请的人是否已经在group里
            if GroupMember.objects.filter(user_id=receiver.id).exists():
                return render(request, 'invite_to_group.html', {'message': "此用户已存在这个团队"})
            else:
                invitation.receiver_name = receiverName
            # 查询这个文档是否存在刚才输入的group里
            # docId = request.POST.get('doc_Id')
            # if Doc.objects.filter(is_group_doc = True).filter(doc_group_id = group_id).exists():
            #     invitation.document_id = docId
            # else:
            #     return render(request,'invite_to_group.html',{'messages':"你的团队中没有这个的文档"})
            invitation.save()
            return redirect('/')
        else:
            return render(request, 'invite_to_group.html')
            # get 请求，刚进邀请人界面
    else:
        return redirect('/login/')


# 查看自己目前有什么组
def mygroup(request):
    # 如果用户已经登录了
    if request.session.get('username'):
        cur_username = request.session['username']
        cur_user = User.objects.get(name=cur_username)
        my_groups = GroupMember.objects.filter(id=cur_user.id)
        my_grouplist = QuerySet()
        for group in my_groups.iterator():
            my_grouplist |= Group.objects.filter(id=group.id)
        # 返回有“我”的团队名
        return render(request, 'mygroup.html', {'username': cur_username, 'my_grouplist': my_groups})
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
            new_group.leader_id = cur_user.id
            new_group.groupname = request.POST.get('groupname')
            new_group.save()

            newGroupMember = GroupMember()
            newGroupMember.group_id = new_group.id
            newGroupMember.user_id = cur_user.id
            newGroupMember.save()
            # POST 请求创建团队成功，返回到自己的group列表
            return redirect(mygroup)
        else:  # 创建团队的页面
            return render(request, 'newgroup.html')
    else:
        return redirect('/login/')


class GroupMemberListView(View):
    """成员列表试图"""

    def get(self, request):
        """查询所有图书接口"""
        # 1. 查询出所有成员模型
        members = GroupMember.objects.all()
        # 2. 遍历查询集，取出里面的每个成员模型对象，把模型对象转换成字典
        # 声明一个变量用来保存所有字典
        member_list = []
        for member in members:
            member_dict = {
                'gid': member.group_id,
                'gmid': member.user_id,
            }
            # 将转换好的字典添加到列表中
            group_member_list.append(group_member_dict)
        # 3. 响应
        return JsonResponse(member_list, safe=False)

    def post(self, request):
        """新增成员接口"""
        # 接收前端数据
        # 1.获取前端传入的json类型请求体： request.body
        json_str_bytes = request.body
        # 2.将bytes类型的json字符串转成json字典/列表
        json_str = json_str_bytes.decode()
        # 3.创建模型对象并保存（把字典转换成模型并存储）
        member_dict = json.loads(json_str)

        # 创建模型对象并保存 （把字典转换成模型并存储）
        member = GroupMember(group_id=member_dict['gid'], user_id=member_dict['user_id'])
        member.save()

        # 把新增的模型转换成字典
        json_dict = {
            'gid': member.group_id,
            'gmid': member.user_id,
        }
        # 响应（除了删除其他必须要有响音）删除响音的码为201
        return JsonResponse
        pass


class GroupMemberDetailView(View):
    """详情视图"""

    def get(self, request, pk):
        """查询所有图书接口"""
        # 1. 查询出所有成员模型
        try:
            members = GroupMember.objects.all()
        except GroupMember.DoesNotExist:
            return HttpResponse({'message': '查询数据不存在'}, status=404)
            # 2. 模型对象转换成字典
        # 声明一个变量用来保存所有字典
        member_dict = {
            'gid': member.group_id,
            'gmid': member.user_id,
        }
        # 3. 响应
        return JsonResponse(group_member_dict)

    def put(self, request, pk):
        """修改接口"""
        # 查询修改对象
        try:
            member = GroupMember.objects.get(pk=pk)
        except GroupMember.DoesNotExist:
            return HttpResponse({'message': '要修改的数据不存在'},status=404)
        # 获取前端传入的新数据（把数据转换成字典）
        json_str_bytes = request.body
        json_str = json_str_bytes.decode()
        member_dict = json.loads(json_str)

        # member_dict = json.loads(request.body.decode())


        #
        pass

    def delete(self, request, pk):
        """删除接口"""
        # 获取要删除的对象
        try:
            member = GroupMember.objects.get(id=pk)
        except GroupMember.DoesNotExist:
            return HttpResponse()
        # 删除对象
        # 物理删除 （真的从数据库中被删除了）
        member.delete()
        # 逻辑删除 （伪删除）
        # member.is_delete = True
        # member.save()
        # 响应：删除时不需要有响应弹药指定状态码为204
        return HttpResponse(status=204)


class GroupMemberView(ModelViewSet):
    """定义类视图"""
    # 指定查询集
    queryset = GroupMember.objects.all()

    # 指定序列化器
    serializer_class = GroupMemberSerializer



