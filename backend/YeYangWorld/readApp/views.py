from django.views.decorators.csrf import csrf_exempt

from django.http import JsonResponse
from django.core.serializers import serialize
import json

from readApp.models import EnglishArticle
from userApp.models import DtwzUser
from myutils import JWT
jwt = JWT()


@csrf_exempt
def upload_article(request):
    if request.method == 'POST':
        token = request.META.get('HTTP_AUTHORIZATION')
        token = token.split(' ')[1]
        userid = jwt.verify_token(token)

        title = request.POST.get('title')
        cover = request.FILES.get('cover')
        content = request.POST.get('content')
        category_id = request.POST.get('category_id')
        #将字符串转化为数字，如果是空字符串则转化为0
        if category_id == '':
            category_id = None
        else:
            category_id = int(category_id)

    
        print(category_id)


        #通过userid查询用户信息
        user = DtwzUser.objects.get(id=userid)
        user_name = user.name

        # 插入数据到EnglishArticle表中
        EnglishArticle.objects.create(title=title, cover=cover, content=content, creator=user_name, category_id=category_id)

        return JsonResponse({'status': 200, 'message': '上传成功'})
    else:
        return JsonResponse({'status': 400, 'message': '请求方法错误'})

@csrf_exempt
def get_articl_list(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        count = data['count']
   
        #按照最新的时间排序，然后取出count到count+10的不含内容与创建事件字段的数据
        article_list = EnglishArticle.objects.all().order_by('-create_time')[count+1:count+10].values('id', 'title', 'cover', 'creator', 'category', 'watch_count', 'star_count')
        article_list = list(article_list)
        count = count + len(article_list)

        return JsonResponse({'status': 200, 'count':count ,'article_list': article_list})
    else:
        return JsonResponse({'status': 400, 'message': '请求方法错误'})


@csrf_exempt
def get_article_detail(request):
    if request.method == 'POST':

        data = json.loads(request.body)
        article_id = data['article_id']

        #根据id查询数据
        article = EnglishArticle.objects.get(id=article_id)
        article = serialize('json', [article], fields=('id', 'title', 'cover', 'content', 'category'))
        article = json.loads(article)[0]['fields']

        return JsonResponse({'status': 200, 'article': article})
    else:
        return JsonResponse({'status': 400, 'message': '请求方法错误'})


