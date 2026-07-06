from django.http import HttpResponse

def index(request):
    print("Student Dashboard")
    return HttpResponse("Student Dashboard")
