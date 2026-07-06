from django.http import HttpResponse

def index(request):
    print("Food Menu")
    return HttpResponse("Food Menu")
