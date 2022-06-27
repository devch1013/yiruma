from django.shortcuts import render, redirect
from django.db.models import Q
from .models import *
from .forms import *
from money.models import *

# Create your views here.


def student_home(request):
  if request.method == 'POST':
    student_del = Studentinfo.objects.get(id=request.POST.get('stu_id'))
    student_del.delete()
    return redirect('student_home')
  
  student = Studentinfo.objects.all()

  content = {'student': student}
  return render(request, 'student/student_home.html', content)


def student_create(request):
  form = StudentForm()
  if request.method == 'POST':
    form = StudentForm(request.POST)
    if form.is_valid():
      obj = form.save(commit=False)
      obj.make_id()
      obj.save()
         
      return redirect('student_home')
  content = {'form':form}
  return render(request, 'student/student_create.html', content)

def student_detail(request, id):
  student = Studentinfo.objects.get(id=id)
  money = Money.objects.filter(student=student)
  content = {'student':student, 'money':money}
  return render(request, 'student/student_detail.html', content)

def student_edit(request, id):
  student = Studentinfo.objects.get(id=id)
  
  if request.method == 'POST':
    form = StudentEditForm(request.POST, instance=student)
    if form.is_valid():
      student = form.save(commit=False)
      student.save()
         
      return redirect('student_home')
  else:
    form = StudentEditForm(instance=student)
  content = {'student':student, 'form':form}
  return render(request, 'student/student_create.html', content)