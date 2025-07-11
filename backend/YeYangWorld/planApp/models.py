from django.db import models
from userApp.models import DtwzUser


# Create your models here.
class PlanCompleted(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(DtwzUser, on_delete=models.CASCADE, db_comment='用户id')
    content = models.TextField(db_comment='计划内容')
    create_time = models.DateField(db_comment='创建时间')

    class Meta:
        managed = True
        db_table = 'planapp_plan_completed'
        #创建时间的索引
        indexes = [
            models.Index(fields=['user','create_time'],name='user_create_time')
        ]
 
