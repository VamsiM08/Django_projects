from django.http import HttpResponse

def index(request):
    print("Class Information")
    return HttpResponse("Class Information")
