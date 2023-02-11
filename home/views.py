from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from home.models import Departments, Employees
from home.serializers import DepartmentSerilizer, EmployeeSerilizer
from django.core.files.storage import default_storage
import json
# Create your views here.


@csrf_exempt
def departmentApi(request, id=0):

    if request.method == 'GET':
        departments = Departments.objects.all()
        departments_serializer = DepartmentSerilizer(departments, many=True)
        return JsonResponse(departments_serializer.data, safe=False)
    elif request.method == 'POST':
        department_Data = JSONParser().parse(request)
        departments_serializer = DepartmentSerilizer(data=department_Data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Added Success Fully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        department_Data = JSONParser().parse(request)
        print(department_Data)
        department = Departments.objects.get(
            DepartmentId=id)
        departments_serializer = DepartmentSerilizer(
            department, data=department_Data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Update Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        department = Departments.objects.get(DepartmentId=id)
        department.delete()
        return JsonResponse("Deleted Successfully", safe=False)


@csrf_exempt
def employeeApi(request, id=0):
    print(id)
    if request.method == 'GET' and id == 0:
        employees = Employees.objects.all()
        employees_serializer = EmployeeSerilizer(employees, many=True)
        return JsonResponse(employees_serializer.data, safe=False)
    elif request.method == 'GET' and id != 0:
        print("hlo word")
        employees = Employees.objects.get(EmployeeId=id)
        employees_serializer = EmployeeSerilizer(employees)
        return JsonResponse(employees_serializer.data, safe=False)
    elif request.method == 'POST':

        imageName = imageSave(request.FILES['file'])
        print(imageName)
        employee_Data = JSONParser().parse(request.KEY['EmployeeName'])
        print(employee_Data)
        employees_serializer = EmployeeSerilizer(data=employee_Data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Added Success Fully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        employee_Data = JSONParser().parse(request)
        employee = Employees.objects.get(
            EmployeeId=id)
        employees_serializer = EmployeeSerilizer(
            employee, data=employee_Data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Update Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        employee = Employees.objects.get(EmployeeId=id)
        employee.delete()
        return JsonResponse("Deleted Successfully", safe=False)


@csrf_exempt
def get_all_employes_of_department(request, id=0):
    if request.method == 'GET':
        print(id)
        employees = Employees.objects.filter(Department=id)
        employees_serializer = EmployeeSerilizer(employees, many=True)
        return JsonResponse(employees_serializer.data, safe=False)


def index(request):
    return HttpResponse("this is home page")


def about(request):
    return HttpResponse("this is about page")


def services(request):
    return HttpResponse('services page')


def imageSave(image):
    file_name = default_storage.save(image.name, image)
    return file_name


@csrf_exempt
def SaveFile(request):
    file = request.FILES['file']
    file_name = default_storage.save(file.name, file)
    return JsonResponse(file_name, safe=False)
