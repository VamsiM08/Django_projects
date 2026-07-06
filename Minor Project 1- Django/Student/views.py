from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.

def student(request):
    """
    Renders Student Home Page.
    Returns JSON if query parameter format=json is specified.
    """
    if request.GET.get('format') == 'json':
        return JsonResponse({"message": "Welcome to Student App"})
    return render(request, 'student/student_home.html')

def student_details(request):
    """
    Returns JSON response for Student Details Page.
    """
    return JsonResponse({"message": "Student Details Page"})

def student_profile(request):
    """
    Returns JSON response for Student Profile Page.
    """
    return JsonResponse({"message": "Student Profile Page"})

def student_id(request, id):
    """
    Returns text response displaying the Student ID.
    """
    return HttpResponse(f"Student ID : {id}")
