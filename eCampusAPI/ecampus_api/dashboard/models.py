from django.db import models

class Module(models.Model):
    name = models.CharField('Module Name', max_length=60)
    description = models.CharField('Module Description', max_length=150)
    rank = models.IntegerField('Priority')
    color = models.CharField('Module Color', max_length=60, null=True)
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
