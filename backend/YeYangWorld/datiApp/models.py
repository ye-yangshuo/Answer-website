from django.db import models

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