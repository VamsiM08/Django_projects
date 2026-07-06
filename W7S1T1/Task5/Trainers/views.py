from django.http import HttpResponse

def index(request):
    print("Trainer Dashboard")
    return HttpResponse("Trainer Dashboard")
