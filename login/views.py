from __future__ import unicode_literals
from django.http import HttpResponse,response
from login.models import Student, Teacher, Answer_table
from django.shortcuts import render, redirect, render_to_response
from django.template import loader, RequestContext
from django.core.files.storage import FileSystemStorage
from xlrd import open_workbook


def index(request):
    if request.method == "POST":
        if 'Student' in request.POST:
            return render(request, 'login_page_student.html')
        elif 'Teacher' in request.POST:
            return render(request, 'login_page_teacher.html')
    return render(request, 'login.html')


def student(request):
    all_students = Student.objects.all()
    # template=loader.get_template('login/index1.html')
    # print (request.POST['LoginID'])
    if request.method == "POST" and request.POST['LoginID'] and request.POST['Password']:
        LoginID = request.POST.get('LoginID', False)
        Password = request.POST.get('Password', False)
        for i in all_students:
            if i.LoginID == LoginID and i.Password == Password:
                #temp=loader.get_template('student_upload.html')
                #ttt={}
                #data=temp.render(ttt,request)
                # response = HttpResponse(render(request, 'student_upload.html'))
                #response.set_cookie('LoginID',LoginID)
                response = render_to_response('student_upload.html', {'LoginID':LoginID})
                response.set_cookie('LoginID',LoginID)
                return response
            # response = HttpResponse("sample")
    return render(request, 'login_page_student.html')


def teacher(request):
    all_teachers = Teacher.objects.all()
    # template=loader.get_template('login/index1.html')
    # print (request.POST['LoginID'])
    if request.method == "POST" and request.POST['LoginID'] and request.POST['Password']:
        LoginID = request.POST.get('LoginID', False)
        Password = request.POST.get('Password', False)
        for i in all_teachers:
            if i.LoginID == LoginID and i.Password == Password:
                return render(request, 'teacher_upload.html')
    return render(request, 'login_page_teacher.html')

def student_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        answers = Answer_table.objects.all()
        correct = 0
        workbook = open_workbook('C:/Users/PRUDHVI/PycharmProjects/quiz/media/' + myfile.name, "r")
        worksheet = workbook.sheet_by_index(0)
        for row in range(1, worksheet.nrows):
            for i in answers:
                if i.Question_no == (int(worksheet.cell(row, 0).value)):
                    if i.Answer_value == (str(worksheet.cell(row, 1).value)):
                        correct += 1
        num=request.COOKIES['LoginID']
        all_students = Student.objects.all()
        for i in all_students:
            if i.LoginID == num:
                i.Score = (int(correct))
                i.save()
        return render(request, 'uploaded_student.html', {'correct': correct})
    return render(request, 'student_upload.html')


def teacher_upload(request):
    if request.method == 'POST' and request.FILES['myfile'] and request.FILES['myfile1']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        myfile1 = request.FILES['myfile1']
        fs1 = FileSystemStorage()
        filename1 = fs1.save(myfile1.name, myfile1)
        uploaded_file_url1 = fs1.url(filename1)
        answers = Answer_table.objects.all()
        workbook = open_workbook('C:/Users/PRUDHVI/PycharmProjects/quiz/media/' + myfile.name, "r")
        worksheet = workbook.sheet_by_index(0)
        for row in range(1, worksheet.nrows):
            for i in answers:
                if i.Question_no == (int(worksheet.cell(row, 0).value)):
                    i.Answer_value = (worksheet.cell(row, 1).value)
                    i.save()
        return render(request, 'uploaded_teacher.html')
    return render(request, 'teacher_upload.html')
