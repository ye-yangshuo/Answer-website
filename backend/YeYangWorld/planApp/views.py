from django.views.decorators.csrf import csrf_exempt

from django.http import JsonResponse
from django.core.serializers import serialize
import json
import datetime

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

        data = json.loads(request.body)
        plan_content = data['plan_content']

        # 插入数据
        PlanCompleted.objects.create(user_id=userid, content=plan_content)
        return JsonResponse({'status': 200, 'message': '提交成功'})
    else:
        return JsonResponse({'status': 400, 'message': '请求方式错误'})


@csrf_exempt
def get_plan(request):
    if request.method == 'GET':
        token = request.META.get('HTTP_AUTHORIZATION')
        token = token.split(' ')[1]
        userid = jwt.verify_token(token)

        currentDate = datetime.date.today()
        # 查询数据
        plans = PlanCompleted.objects.filter(user_id=userid,create_time__year=currentDate.year, create_time__month=currentDate.month)
        plans_data = [{'id': plan.id, 'content': plan.content, 'create_time': plan.create_time} for plan in plans]

        print(plans_data)
        return JsonResponse({'status': 200, 'data': plans_data})