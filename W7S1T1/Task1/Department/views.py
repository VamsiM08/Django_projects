from django.http import HttpResponse

def index(request):
    print("This is Department")
    return HttpResponse("This is Department")
