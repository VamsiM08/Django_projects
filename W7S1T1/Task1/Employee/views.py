from django.http import HttpResponse

def index(request):
    print("This is Employee")
    return HttpResponse("This is Employee")
