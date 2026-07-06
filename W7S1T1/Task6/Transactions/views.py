from django.http import HttpResponse

def index(request):
    print("Transaction History")
    return HttpResponse("Transaction History")
