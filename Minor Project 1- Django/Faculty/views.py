from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.

def faculty(request):
    """
    Renders Faculty Home Page.
    Returns JSON if query parameter format=json is specified.
    """
    if request.GET.get('format') == 'json':
        return JsonResponse({"message": "Welcome to Faculty App"})
    return render(request, 'faculty/faculty_home.html')

def faculty_details(request):
    """
    Returns JSON response for Faculty Details Page.
    """
    return JsonResponse({"message": "Faculty Details Page"})

def faculty_profile(request):
    """
    Returns JSON response for Faculty Profile Page.
    """
    return JsonResponse({"message": "Faculty Profile Page"})

def faculty_name(request, name):
    """
    Returns text response displaying the Faculty Name.
    """
    return HttpResponse(f"Faculty Name : {name}")
