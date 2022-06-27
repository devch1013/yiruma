from django.shortcuts import render, redirect
from django.db.models import Q
from .models import *
from .forms import *
# from .forms import *

# Create your views here.
def money_home(request):
  q = request.GET.get('q') if request.GET.get('q') != None else ''
  
  month = request.GET.get('month') if request.GET.get('month') != None else ''

  if 'unpay' in q:
    money = Money.objects.filter(Q(get_check=False) & Q(pay_check = False))
  elif 'unget' in q:
    money = Money.objects.filter(get_check=False)
  
  else:
    money = Money.objects.all()

  if request.method == 'POST':
    if request.POST.get('month_data'):
      month_data = request.POST.get('month_data')
      print(month_data)
      make_month_list(month_data)   
      return redirect('.')

    elif request.POST.get('money_id'):
      money_del = Money.objects.get(id=request.POST.get('money_id'))
      money_del.delete()
      return redirect('.')
         
  

  content = {'money': money}
  return render(request, 'money/money_home.html', content)


def money_detail(request, id):
  money = Money.objects.get(id=id)
  content = {'money':money}
  return render(request, 'money/money_detail.html', content)

def money_create(request):
  form = MoneyForm()
  if request.method == 'POST':
    form = MoneyForm(request.POST)
    if form.is_valid():
      obj = form.save(commit=False)
      obj.make_id()
      obj.save()
         
      return redirect('money_home')
  content = {'form':form}
  return render(request, 'money/money_create.html', content)


def money_edit(request, id):
  money = Money.objects.get(id=id)
  
  if request.method == 'POST':
    form = MoneyForm(request.POST, instance=money)
    if form.is_valid():
      money = form.save(commit=False)
      money.save()
         
      return redirect('money_home')
  else:
    form = MoneyForm(instance=money)
  content = {'money':money, 'form':form}
  return render(request, 'money/money_create.html', content)