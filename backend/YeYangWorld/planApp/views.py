from django.views.decorators.csrf import csrf_exempt

from django.http import JsonResponse
from django.core.serializers import serialize
import json

from userApp.models import DtwzUser
from planApp.models import PlanCompleted
from myutils import JWT
jwt = JWT()

@csrf_exempt
def commit_plan(request):
    if request.method == 'POST':
        token = request.META.get('HTTP_AUTHORIZATION')
        token = token.split(' ')[1]
        userid = jwt.verify_token(token)
        print(userid)
        data = json.loads(request.body)
        plan_content = data['plan_content']

        # 插入数据
        PlanCompleted.objects.create(user_id=userid, content=plan_content)
        return JsonResponse({'status': 200, 'message': '提交成功'})
    else:
        return JsonResponse({'status': 400, 'message': '请求方式错误'})


