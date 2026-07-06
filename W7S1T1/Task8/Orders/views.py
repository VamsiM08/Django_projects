from django.http import HttpResponse

def index(request):
    print("Order Details")
    return HttpResponse("Order Details")
