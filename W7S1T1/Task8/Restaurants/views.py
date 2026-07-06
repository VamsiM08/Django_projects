from django.http import HttpResponse

def index(request):
    print("Restaurant List")
    return HttpResponse("Restaurant List")
