from django.http import HttpResponse

def index(request):
    print("Available Courses")
    return HttpResponse("Available Courses")
