from cProfile import label
from django.forms import ModelForm
from django import forms
from .models import *
import datetime as dt

class MoneyForm(ModelForm):
  student = forms.ModelChoiceField(queryset=Studentinfo.objects.all(), label='학생')
  pay_date = forms.DateTimeField(label='결제일', widget=forms.DateInput(attrs={'type': 'date'}),required=False)
  get_date = forms.DateTimeField(label='확인일', widget=forms.DateInput(attrs={'type': 'date'}),required=False)
  due = forms.IntegerField(label='회비',required=False)
  class Meta:
    model = Money
    fields = '__all__'
    exclude = ['id']