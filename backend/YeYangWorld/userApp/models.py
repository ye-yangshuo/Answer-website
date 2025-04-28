from django.db import models

# Create your models here.

class DtwzUser(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32, blank=False, null=False, db_comment='用户名')
    password = models.CharField(max_length=32, blank=False, null=False, db_comment='用户密码')
    email = models.CharField(max_length=32, blank=False, null=False, db_comment='用户邮箱')
    phone = models.CharField(max_length=32, blank=False, null=False, db_comment='用户手机号')
    #头像图片
    avatar = models.ImageField(upload_to='userAPP/avatar', blank=True, null=True, db_comment='用户头像')
    
    
    class Meta:
        managed = True
        db_table = 'dtwz_user'
        db_table_comment = '用户管理表'
        
  