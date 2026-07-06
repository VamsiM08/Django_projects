from django.http import HttpResponse

def index(request):
    print("This is Patient")
    return HttpResponse("This is Patient")
