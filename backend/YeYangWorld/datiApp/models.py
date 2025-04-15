from django.db import models
from userApp.models import DtwzUser
# Create your models here.
class DtwzProblem(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.TextField(blank=True, null=True)
    option_a = models.TextField(blank=True, null=True)
    option_b = models.TextField(blank=True, null=True)
    option_c = models.TextField(blank=True, null=True)
    option_d = models.TextField(blank=True, null=True)
    answer = models.TextField(blank=True, null=True)
    explanation = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'dtwz_problem'

class DTWZProblemCompleted(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(DtwzUser,on_delete=models.CASCADE,db_comment='用户id')
    problem = models.ForeignKey(DtwzProblem,on_delete=models.CASCADE,db_comment='题目id')
    istrue = models.BooleanField(db_comment='是否正确')
    collection = models.BooleanField(db_comment='是否收藏')
    note = models.TextField(blank=True, null=True, db_comment='用户笔记')

    class Meta:
        managed = True
        db_table = 'dtwz_problem_completed'
        indexes = [
            models.Index(fields=['user', 'problem'], name='user_problem')
        ]


