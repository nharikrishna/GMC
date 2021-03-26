from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .models import *


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_type = request.POST.get('type')
        name = ""
        flag = 0
        if user_type == 'student':
            users = Student.objects.all()
            for e in users:
                if e.username == username:
                    name = e.first_name + e.last_name
                    flag = 1
                    break
        elif user_type == 'advisor':
            users = Advisor.objects.all()
            for e in users:
                if e.username == username:
                    name = e.first_name + e.last_name
                    flag = 1
                    break
        elif user_type == 'faculty':
            users = Faculty.objects.all()
            for e in users:
                if e.username == username:
                    flag = 1
                    break

        else:
            '''
            users = Faculty.objects.all()
            for e in users:
                if e.username == username:
                    name = e.name
                    flag = 1
                    break
            '''

        user = authenticate(request, username=username, password=password)

        if user is not None and flag == 1:
            login(request, user)
            if user_type == 'student':
                return redirect(view_profile_student_view)
            elif user_type == 'advisor':
                return redirect(view_profile_advisor_view)
            elif user_type == 'faculty':
                return redirect(view_profile_faculty_view)
            else:
                return redirect(login_view)
        else:
            messages.info(request, 'Username or password is incorrect')

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect(login_view)


def check_view(request):
    return render(request, 'check.html')


def view_profile_advisor_view(request):
    username = request.user.username
    entry = Advisor.objects.get(username=username)
    first_name = entry.first_name
    last_name = entry.last_name
    year = entry.year

    context = {'username': username, 'first_name': first_name, 'last_name': last_name, 'year': year}

    return render(request, 'Advisor/view_profile.html', context)


def class_details_view(request):
    username = request.user.username
    entry1 = Advisor.objects.get(username=username)
    year = entry1.year

    entry2 = Student.objects.filter(year=year)
    context = {'e1': entry1, 'e2': entry2}
    return render(request, 'Advisor/class_details.html', context)


def view_profile_student_view(request):
    username = request.user.username
    entry1 = Student.objects.get(username=username)
    context = {'e1': entry1}
    return render(request, 'Student/view_profile_student.html', context)


def view_marks_view(request):
    username = request.user.username
    entry1 = Student.objects.get(username=username)
    year = entry1.year

    entry2 = Course.objects.filter(year=year)
    for e in entry2:
        print(e.course_title)
    context = {'e1': entry1, 'e2': entry2}
    return render(request, 'Student/view_marks.html', context)


def view_profile_faculty_view(request):
    username = request.user.username
    entry1 = Faculty.objects.get(username=username)
    context = {'e1': entry1}
    return render(request, 'Faculty/view_profile_faculty.html', context)


def view_course_faculty_view(request):
    username = request.user.username
    entry1 = Faculty.objects.get(username=username)
    entry2 = FacultyCourse.objects.filter(username=username)
    for i in entry2:
        print(i.course_title_id)
    context = {'e1': entry1, 'e2': entry2}
    return render(request, 'Faculty/view_course.html', context)


def view_marks_faculty_view(request):
    username = request.user.username
    entry1 = Faculty.objects.get(username=username)
    context = {'e1': entry1}
    return render(request, 'Faculty/view_marks.html', context)


def update_marks_view(request):
    username = request.user.username
    entry1 = Faculty.objects.get(username=username)

    context = {'e1': entry1}
    return render(request, 'Faculty/update_marks.html', context)
