from django.conf import settings
from django.db import models
from django.utils import timezone


class Account(models.Model):
    id = models.CharField(max_length=32, unique=True,primary_key=True,verbose_name='ID')
    password = models.CharField(max_length=20, verbose_name='PASSWORD')
    created_date = models.DateTimeField(
            default=timezone.now,verbose_name="계정 생성일")
    email = models.EmailField(max_length=128, unique=True, verbose_name='이메일')
    name = models.CharField(max_length=32,verbose_name="이름")
    watched_drama = models.TextField(default='')
    def __str__(self):
        return self.id
    
    class Meta:
        db_table = 'Account'
        verbose_name='유저'
        verbose_name_plural='유저'

#사용자가 본 드라마
class DRAMA(models.Model):
    drama_name = models.CharField(max_length=30,unique=True,verbose_name='드라마 제목')
    drama_id =models.IntegerField(primary_key=True,verbose_name='드라마 아이디')
    class Meta:
        db_table = 'DRAMA'
        verbose_name='DRAMA'
        verbose_name_plural='DRAMA'
        
    def __str__(self):
        return self.drama_name