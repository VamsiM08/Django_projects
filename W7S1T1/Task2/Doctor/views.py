from django.http import HttpResponse

def index(request):
    print("This is Doctor")
    return HttpResponse("This is Doctor")
