from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

# --- Template Views ---

def patient_home(request):
    return render(request, 'patient.html')

def patient_details(request):
    return render(request, 'patient_details.html')

def patient_report(request):
    return render(request, 'patient_report.html')

def patient_bill(request):
    return render(request, 'patient_bill.html')


# --- REST API Views ---

@csrf_exempt
def patient_home_api(request):
    if request.method == 'GET':
        return JsonResponse({"message": "Welcome to Patient API"})
    return JsonResponse({"error": "Only GET method is allowed"}, status=405)

@csrf_exempt
def patient_details_api(request):
    if request.method == 'GET':
        return JsonResponse({
            "patient_id": "P201",
            "patient_name": "Rahul Sharma",
            "age": 28,
            "gender": "Male",
            "disease": "Viral Fever"
        })
    return JsonResponse({"error": "Only GET method is allowed"}, status=405)

@csrf_exempt
def add_patient_api(request):
    if request.method == 'POST':
        return JsonResponse({"message": "Patient Added Successfully"})
    return JsonResponse({"error": "Only POST method is allowed"}, status=405)

@csrf_exempt
def update_patient_api(request):
    if request.method == 'PUT':
        return JsonResponse({"message": "Patient Updated Successfully"})
    return JsonResponse({"error": "Only PUT method is allowed"}, status=405)

@csrf_exempt
def delete_patient_api(request):
    if request.method == 'DELETE':
        return JsonResponse({"message": "Patient Deleted Successfully"})
    return JsonResponse({"error": "Only DELETE method is allowed"}, status=405)


# --- Dynamic URL Views ---

def patient_by_id(request, patient_id):
    return HttpResponse(f"Patient ID : {patient_id}")

def patient_by_name(request, patient_name):
    return HttpResponse(f"Patient Name : {patient_name}")
