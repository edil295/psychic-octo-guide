from django.shortcuts import render
from .models import Course, Student
from django.http import HttpResponse
from .forms import CourseForm, StudentForm


def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})


def course_add(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Success')
        else:
            return HttpResponse('Error')
    if request.method == 'GET':
        form = CourseForm()
        return render(request, 'course_add.html', {'form': form})


def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})


def student_add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Успешно')
        else:
            return HttpResponse('Ошибка')
    if request.method == 'GET':
        form = StudentForm()
        return render(request, 'student_add.html', {'form': form})