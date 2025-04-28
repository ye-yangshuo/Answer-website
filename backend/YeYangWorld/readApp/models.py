from django.db import models

class Category(models.Model): #文章分类
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, db_comment='分类名称')
    class Meta:
        managed = True
        db_table ='readapp_category'



class EnglishArticle(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=256, db_comment='标题')
    cover = models.ImageField(blank=True,null=True,upload_to='readApp/english_article', db_comment='封面图片')
    content = models.TextField(db_comment='内容')
    creator = models.CharField(max_length=64, db_comment='创建者')
    create_time = models.DateTimeField(auto_now_add=True, db_comment='创建时间')
    category = models.ForeignKey(Category,on_delete=models.SET_NULL, db_comment='分类id', null=True, blank=True)
    watch_count = models.IntegerField(default=0, db_comment='观看次数')
    star_count = models.IntegerField(default=0, db_comment='收藏次数')
    class Meta:
        managed = True
        db_table ='readapp_english_article'






