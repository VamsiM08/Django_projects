from django.http import HttpResponse

def index(request):
    print("Loan Details")
    return HttpResponse("Loan Details")
