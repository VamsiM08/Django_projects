from django.http import HttpResponse

def index(request):
    print("Teacher Information")
    return HttpResponse("Teacher Information")
