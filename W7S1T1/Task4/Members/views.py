from django.http import HttpResponse

def index(request):
    print("Member Information")
    return HttpResponse("Member Information")
