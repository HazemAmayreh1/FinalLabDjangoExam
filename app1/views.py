from django.shortcuts import render, redirect
from .models import *
from .forms import StudentForm

def dashboard(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = StudentForm()

    students = Student.objects.all()
    context = {
        'form': form,
        'students': students,
    }
    return render(request, 'app1/dashboard.html', context)

def student_add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'app1/dashboard.html', {'form': form})

def student_edit(request, id):
    student = Student.objects.get(pk=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = StudentForm(instance=student)
    return render(request, 'app1/edit_student.html', {'form': form})


def student_delete(request, id):
    student = Student.objects.get(pk=id)
    if request.method == 'POST':
        student.delete()
        return redirect('dashboard')
    return render(request, 'app1/delete_student.html', {'student': student})

