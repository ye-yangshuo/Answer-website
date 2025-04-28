from django.views.decorators.csrf import csrf_exempt

from django.http import JsonResponse
from django.core.serializers import serialize
import json

from readApp.models import EnglishArticle
from myutils import JWT
jwt = JWT()

@csrf_exempt
def upload_article(request):
    if request.method == 'POST':
        token = request.META.get('HTTP_AUTHORIZATION')
        token = token.split(' ')[1]
        userid = jwt.verify_token(token)

        data = json.loads(request.body)
        print(data)
        title = data['title']
        cover = data['cover']
        content = data['content']
        category_id = data['category_id']
        
        # 插入数据到EnglishArticle表中
        EnglishArticle.objects.create(title=title, cover=cover, content=content, creator=userid, category=category_id)

        return JsonResponse({'status': 200, 'message': '上传成功'})
    else:
        return JsonResponse({'status': 400, 'message': '请求方法错误'})


