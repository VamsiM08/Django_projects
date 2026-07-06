from django.http import HttpResponse

def index(request):
    print("Student Information")
    return HttpResponse("Student Information")
