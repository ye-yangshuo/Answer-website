from django.views.decorators.csrf import csrf_exempt

from django.http import JsonResponse
from userApp.models import DtwzUser

# Create your views here.
@csrf_exempt
def login_verify(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = DtwzUser.objects.get(name=username, password=password)
            return JsonResponse({'status': 'success', 'message': '登录成功', 'user_id': user.id})
        except DtwzUser.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': '用户名或密码无效'})
    else:
        return JsonResponse({'status': 'error', 'message': '无效的请求方法'})

@csrf_exempt
def sendcode(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        #TODO
        #验证邮箱格式是否正确
        #发送验证码到邮箱

        return JsonResponse({'status': 'success', 'message': '验证码已发送'})
    else:
        return JsonResponse({'status': 'error', 'message': '无效的请求方法'})

@csrf_exempt
def register_verify(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        code = request.POST.get('code')
        phone = request.POST.get('phone')

        #TODO
        #验证验证码是否正确，用户名是否已存在
        #录入数据
        