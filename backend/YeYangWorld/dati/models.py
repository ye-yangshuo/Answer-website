from django.db import models



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



class DtwzUserInformation(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128, blank=True, null=True, db_comment='用户名')
    password = models.CharField(max_length=32, blank=True, null=True, db_comment='用户密码')
    touxiang = models.TextField(blank=True, null=True, db_comment='用户头像')

    class Meta:
        managed = True
        db_table = 'dtwz_user_information'
        db_table_comment = '用户信息管理'
