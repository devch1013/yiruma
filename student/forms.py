from django.forms import ModelForm
from django import forms
from .models import Studentinfo
import datetime as dt

class StudentForm(ModelForm):
  name = forms.CharField(max_length=10, required=True, label='이름', error_messages={'required': '이름을 입력해 주세요'})
  regi_date = forms.DateTimeField(label='등록일', widget=forms.DateInput(attrs={'type': 'date'}), initial=dt.datetime.now())
  due_date = forms.DateTimeField(label='회비일', widget=forms.DateInput(attrs={'type': 'date'}), initial=dt.datetime.now())
  sch_year = forms.ChoiceField(label='학년', choices=Studentinfo.SCH_YEAR_CHOICES)
  phone = forms.CharField(max_length=20, label='연락처', required=False)
  payment_method = forms.ChoiceField(label='결제 수단', choices=Studentinfo.PAY_METHOD, widget= forms.Select(attrs={'onchange':'changeSelect(this)'}))
  memo = forms.CharField(widget=forms.Textarea,required=False)
  due = forms.IntegerField(label='회비',required=False)
  card_number = forms.CharField(label='카드 번호',required=False)
  card_bank = forms.CharField(label='은행',required=False)
  class Meta:
    
    
    model = Studentinfo
    fields = '__all__'
    exclude = ['id']
 
  
class StudentEditForm(ModelForm):
  name = forms.CharField(max_length=10, required=True, label='이름', error_messages={'required': '이름을 입력해 주세요'})
  regi_date = forms.DateTimeField(label='등록일', widget=forms.DateInput(attrs={'type': 'date'}))
  due_date = forms.DateTimeField(label='회비일', widget=forms.DateInput(attrs={'type': 'date'}))
  sch_year = forms.ChoiceField(label='학년', choices=Studentinfo.SCH_YEAR_CHOICES)
  phone = forms.CharField(max_length=20, label='연락처', required=False)
  payment_method = forms.ChoiceField(label='결제 수단', choices=Studentinfo.PAY_METHOD, widget= forms.Select(attrs={'onchange':'changeSelect(this)'}))
  memo = forms.CharField(widget=forms.Textarea,required=False)
  due = forms.IntegerField(label='회비',required=False)
  card_number = forms.CharField(label='카드 번호',required=False)
  card_bank = forms.CharField(label='은행',required=False)
  class Meta:
    
    
    model = Studentinfo
    exclude = ['id']
    fields = '__all__'