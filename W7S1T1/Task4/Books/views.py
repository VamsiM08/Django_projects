from django.http import HttpResponse

def index(request):
    print("Book Information")
    return HttpResponse("Book Information")
