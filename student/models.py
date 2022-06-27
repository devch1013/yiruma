from django.db import models
from django.utils.timezone import now

# Create your models here.

class Studentinfo(models.Model):
  def __str__(self):
    return self.id + '  --  ' +self.name
  SCH_YEAR_CHOICES = [
        ('1', '초등학교 1학년'),
        ('2', '초등학교 2학년'),
        ('3', '초등학교 3학년'),
        ('4', '초등학교 4학년'),
        ('5', '초등학교 5학년'),
        ('6', '초등학교 6학년'),
        ('7', '중학교 1학년'),
        ('8', '중학교 2학년'),
        ('9', '중학교 3학년'),
        ('10', '고등학교 1학년'),
        ('11', '고등학교 2학년'),
        ('12', '고등학교 3학년'),
    ]

  PAY_METHOD = [
    ('noty', '미정'),
    ('cash', '현금결제(영수증X)'),
    ('crsp', '현금결제(영수증O)'),
    ('card', '카드결제'),
    ('zero', '제로페이')
  ]
  id = models.CharField(max_length=4, primary_key=True)
  name = models.CharField(max_length=50, null=True, blank=True)
  regi_date = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True, default=now)
  due_date = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
  sch_year = models.CharField(max_length=50, choices=SCH_YEAR_CHOICES, default=None, null=True)
  phone = models.CharField(max_length=11, null=True, blank=True)
  due = models.IntegerField(null=True, blank=True)
  payment_method = models.CharField(max_length=50, choices=PAY_METHOD, default=None, null=True)
  card_number = models.CharField(max_length=20, null=True, blank=True)
  card_bank = models.CharField(max_length=10, null=True, blank=True)
  memo = models.TextField(null=True, blank=True)

  def make_id(self):
    idlist=[]
    if Studentinfo.objects.last():
      for i in Studentinfo.objects.all():
        idlist.append(i.id)
      self.id = "%04d"%(int(max(idlist)) + 1)
      print(idlist)
    else:
      self.id = "0000"

  