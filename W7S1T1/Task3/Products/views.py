from django.http import HttpResponse

def index(request):
    print("Welcome to Products")
    return HttpResponse("Welcome to Products")
