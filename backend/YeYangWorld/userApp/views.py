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
