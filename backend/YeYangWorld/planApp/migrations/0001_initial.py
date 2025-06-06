# Generated by Django 4.2.18 on 2025-05-17 10:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userApp', '0002_alter_dtwzuser_avatar'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlanCompleted',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(db_comment='计划内容')),
                ('create_time', models.DateField(auto_now_add=True, db_comment='创建时间')),
                ('user', models.ForeignKey(db_comment='用户id', on_delete=django.db.models.deletion.CASCADE, to='userApp.dtwzuser')),
            ],
            options={
                'db_table': 'planApp_plan_completed',
                'managed': True,
                'indexes': [models.Index(fields=['user', 'create_time'], name='user_create_time')],
            },
        ),
    ]
