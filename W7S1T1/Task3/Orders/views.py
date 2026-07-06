from django.http import HttpResponse

def index(request):
    print("Welcome to Orders")
    return HttpResponse("Welcome to Orders")
