from django.views.decorators.csrf import csrf_exempt

from django.http import JsonResponse
from datiApp.models import DtwzProblem
from django.core.serializers import serialize
import json

from datiApp.models import DtwzProblem,DTWZProblemCompleted
from myutils import JWT
jwt = JWT()


@csrf_exempt
def get_problem(request):
    if request.method == 'GET':
        token = request.META.get('HTTP_AUTHORIZATION')
        token = token.split(' ')[1]
        userid = jwt.verify_token(token)

        #先根据id查询用户完成表，按照完成id排序，然后根据题目id查询题目表
        dtwz_problem_completed = DTWZProblemCompleted.objects.filter(user_id=userid)

        if(dtwz_problem_completed.exists()):
            #获取完成表中最新的题目id
            dtwz_problem_completed = dtwz_problem_completed.order_by('-problem_id')
            max_problem_id = dtwz_problem_completed[0].problem_id
            print(max_problem_id)
            #获取当前与下一个题目
            now_problem = DtwzProblem.objects.get(id=max_problem_id+1) 
            now_problem = serialize('json', [now_problem])
            now_problem = json.loads(now_problem)
            now_problem_content = now_problem[0]['fields'] 
            now_problem_id = now_problem[0]['pk']
            print(now_problem)
            return JsonResponse({'status': 200,'now_problem_content': now_problem_content, 'now_problem_id': now_problem_id})
        else:
            #获取问题表中最小id与下一个的题目
            now_problem = DtwzProblem.objects.order_by('id')[0]
            now_problem = serialize('json', [now_problem])
            now_problem = json.loads(now_problem)
            now_problem_content = now_problem[0]['fields'] 
            now_problem_id = now_problem[0]['pk']
            return JsonResponse({'status': 200, 'now_problem_content': now_problem_content, 'now_problem_id': now_problem_id})



@csrf_exempt
def submit_problem(request):
    if request.method == 'POST':
        token = request.META.get('HTTP_AUTHORIZATION')
        token = token.split(' ')[1]
        userid = jwt.verify_token(token)

        data = json.loads(request.body)
        problem_id = data['problem_id']
        istrue = data['istrue']
        note = data['note']
        collection = data['iscollect']

        #插入数据到dtwz_problem_completed表中
        DTWZProblemCompleted.objects.create(user_id=userid, problem_id=problem_id, istrue=istrue, note=note, collection=collection)
        return JsonResponse({'status': 200})
