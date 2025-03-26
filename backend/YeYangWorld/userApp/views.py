from django.views.decorators.csrf import csrf_exempt

from django.http import JsonResponse
from userApp.models import DtwzUser
import json

from myutils import Email

#登入验证
@csrf_exempt
def login_verify(request):
    
    if request.method == 'POST':

        data = json.loads(request.body)
        username = data['username']
        password = data['password']
        
        try:
            user = DtwzUser.objects.get(name=username, password=password)
            return JsonResponse(
                {'status': 'success', 
                 'message': '登录成功', 
                 'username': user.name})
        except DtwzUser.DoesNotExist:
            return JsonResponse(
                {'status': 'error',
                 'message': '账号或密码错误'})
        
    else:
        return JsonResponse({'status': 'error', 'message': '无效的请求方法'})

#发送验证码
@csrf_exempt
def send_code(request):
    if request.method == 'POST':

        data = json.loads(request.body)
        to_email = data['email']
        email = Email(to_email = to_email)

        code = email.send_code()
        request.session['code'] = code

        return JsonResponse({'status': 'success', 'message': '验证码发送成功'})
    else:
        return JsonResponse({'status': 'error', 'message': '无效的请求方法'})

#注册验证
@csrf_exempt
def register_verify(request):
    if request.method == 'POST':

        data = json.loads(request.body)
        username = data['username']
        password = data['password']
        email = data['email']
        code = data['code']
        phone = data['phone']

        expire_time = request.session.get_expiry_age() 
        session_code = request.session.get('code')

        if code == session_code and expire_time > 0:
        # 检查用户名是否已存在
            try:
                user = DtwzUser.objects.get(name=username)
                # 如果用户已存在，返回错误信息
                return JsonResponse({'status': 'error', 'message': '用户名已存在'})
            except DtwzUser.DoesNotExist:
            # 用户名不存在，创建新用户
                user = DtwzUser.objects.create(name=username, password=password, email=email, phone=phone)
                return JsonResponse({'status': 'success', 'message': '注册成功', 'user_id': user.id})
        else:
        # 验证码错误或已过期
            return JsonResponse({'status': 'error', 'message': '验证码错误或已过期'})
        #录入数据
        
