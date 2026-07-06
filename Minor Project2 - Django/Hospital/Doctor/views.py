from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

# --- Template Views ---

def doctor_home(request):
    return render(request, 'doctor.html')

def doctor_details(request):
    return render(request, 'doctor_details.html')

def doctor_profile(request):
    return render(request, 'doctor_profile.html')

def doctor_contact(request):
    return render(request, 'doctor_contact.html')


# --- REST API Views ---

@csrf_exempt
def doctor_home_api(request):
    if request.method == 'GET':
        return JsonResponse({"message": "Welcome to Doctor API"})
    return JsonResponse({"error": "Only GET method is allowed"}, status=405)

@csrf_exempt
def doctor_details_api(request):
    if request.method == 'GET':
        return JsonResponse({
            "doctor_id": "D101",
            "doctor_name": "Dr. Ramesh Kumar",
            "specialization": "Cardiologist",
            "experience": "12 Years",
            "hospital": "City Hospital"
        })
    return JsonResponse({"error": "Only GET method is allowed"}, status=405)

@csrf_exempt
def add_doctor_api(request):
    if request.method == 'POST':
        return JsonResponse({"message": "Doctor Added Successfully"})
    return JsonResponse({"error": "Only POST method is allowed"}, status=405)

@csrf_exempt
def update_doctor_api(request):
    if request.method == 'PUT':
        return JsonResponse({"message": "Doctor Updated Successfully"})
    return JsonResponse({"error": "Only PUT method is allowed"}, status=405)

@csrf_exempt
def delete_doctor_api(request):
    if request.method == 'DELETE':
        return JsonResponse({"message": "Doctor Deleted Successfully"})
    return JsonResponse({"error": "Only DELETE method is allowed"}, status=405)


# --- Dynamic URL Views ---

def doctor_by_id(request, doctor_id):
    return HttpResponse(f"Doctor ID : {doctor_id}")

def doctor_by_name(request, doctor_name):
    return HttpResponse(f"Doctor Name : {doctor_name}")
