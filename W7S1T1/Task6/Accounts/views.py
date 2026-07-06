from django.http import HttpResponse

def index(request):
    print("Account Details")
    return HttpResponse("Account Details")
