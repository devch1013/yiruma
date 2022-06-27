from django.db import models
from django.db.models.deletion import CASCADE
from django.utils.timezone import now
from django.db.models import Q
from student.models import *
# Create your models here.

class Money(models.Model):
  def __str__(self):
    if self.pay_check:
      pc = '지불완료'
    else:
      pc = '지불 미완료'
    if self.get_check:
      gc = '승인 완료'
    else:
      gc = '승인 미완료'
    return '{} -- {} -- {} -- {}, {}'.format(self.id, self.student.name, self.pay_date, pc,gc )
  PAY_METHOD = [
    ('cash', '현금결제(영수증X)'),
    ('crsp', '현금결제(영수증O)'),
    ('card', '카드결제'),
    ('zero', '제로페이')
  ]
  id = models.CharField(max_length=8, primary_key=True)
  student = models.ForeignKey(Studentinfo, on_delete=CASCADE)
  pay_month = models.CharField(max_length=7,null=True, blank=True)
  pay_date = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
  get_date = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
  card_bank = models.CharField(max_length=50, null=True, blank=True)
  card_number = models.CharField(max_length=50, null=True, blank=True)
  due = models.IntegerField(null=True, blank=True)
  pay_check = models.BooleanField(default=False)
  get_check = models.BooleanField(default=False)
  payment_method = models.CharField(max_length=50, choices=PAY_METHOD, default=None, null=True)
  memo = models.TextField(blank=True, null=True)

  def make_id(self):
    idlist=[]
    if Money.objects.last():
      for i in Money.objects.all():
        idlist.append(i.id)
      self.id = "%08d"%(int(max(idlist)) + 1)
      print(idlist)
    else:
      self.id = "00000000"

def make_month_list(month):
  all_student = Studentinfo.objects.all()
  for i in all_student:
    if len(Money.objects.filter(Q(student=i)&Q(pay_month=month))) == 0:
      new = Money()
      new.make_id()
      new.student=i
      new.pay_month = month
      new.payment_method = i.payment_method
      new.card_bank = i.card_bank
      new.card_number = i.card_number
      new.due = i.due
      new.save()
    

