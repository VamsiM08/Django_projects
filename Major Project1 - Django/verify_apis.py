import urllib.request
import urllib.error
import json
import time

BASE_URL = "http://127.0.0.1:8009"

def send_request(path, method='GET', data=None):
    url = f"{BASE_URL}{path}"
    req = urllib.request.Request(url, method=method)
    req.add_header('Content-Type', 'application/json')
    req.add_header('Accept', 'application/json')
    
    body = None
    if data is not None:
        body = json.dumps(data).encode('utf-8')
        
    try:
        with urllib.request.urlopen(req, data=body) as response:
            res_body = response.read().decode('utf-8')
            status_code = response.status
            try:
                res_data = json.loads(res_body)
            except json.JSONDecodeError:
                res_data = res_body
            return status_code, res_data
    except urllib.error.HTTPError as e:
        res_body = e.read().decode('utf-8')
        try:
            res_data = json.loads(res_body)
        except json.JSONDecodeError:
            res_data = res_body
        return e.code, res_data
    except urllib.error.URLError as e:
        print(f"Error connecting to server at {url}: {e.reason}")
        return 0, None

def test_doctors():
    print("\n--- Testing Doctor APIs ---")
    
    # 1. Add Doctor 1
    doc1 = {
        "doctor_name": "Dr. Ramesh Kumar",
        "specialization": "Cardiologist",
        "experience": 12,
        "phone": "9876543210",
        "email": "ramesh@gmail.com",
        "consultation_fee": 700
    }
    code, res = send_request("/doctors/add/", "POST", doc1)
    print(f"POST /doctors/add/ (Doctor 1): Status {code}, Response: {res}")
    assert code == 201, f"Expected 201, got {code}"
    doc1_id = res['id']
    
    # 2. Add Doctor 2
    doc2 = {
        "doctor_name": "Dr. Priya Sharma",
        "specialization": "Dermatologist",
        "experience": 8,
        "phone": "9876543222",
        "email": "priya@gmail.com",
        "consultation_fee": 500
    }
    code, res = send_request("/doctors/add/", "POST", doc2)
    print(f"POST /doctors/add/ (Doctor 2): Status {code}, Response: {res}")
    assert code == 201, f"Expected 201, got {code}"
    doc2_id = res['id']
    
    # 3. Get all Doctors
    code, res = send_request("/doctors/", "GET")
    print(f"GET /doctors/: Status {code}, Total Doctors: {len(res)}")
    assert code == 200, f"Expected 200, got {code}"
    
    # 4. Update Doctor 1
    doc1_updated = doc1.copy()
    doc1_updated['consultation_fee'] = 800
    code, res = send_request(f"/doctors/update/{doc1_id}/", "PUT", doc1_updated)
    print(f"PUT /doctors/update/{doc1_id}/: Status {code}, Response: {res}")
    assert code == 200, f"Expected 200, got {code}"
    assert res['consultation_fee'] == 800
    
    # 5. Delete Doctor 2
    code, res = send_request(f"/doctors/delete/{doc2_id}/", "DELETE")
    print(f"DELETE /doctors/delete/{doc2_id}/: Status {code}, Response: {res}")
    assert code == 200, f"Expected 200, got {code}"
    
    # 6. Verify Delete
    code, res = send_request("/doctors/", "GET")
    print(f"GET /doctors/ (after delete): Status {code}, Total Doctors: {len(res)}")
    assert code == 200, f"Expected 200, got {code}"
    assert not any(d['id'] == doc2_id for d in res), "Doctor 2 should have been deleted"

def test_patients():
    print("\n--- Testing Patient APIs ---")
    
    # 1. Add Patient 1
    pat1 = {
        "patient_name": "Rahul Sharma",
        "age": 28,
        "gender": "Male",
        "phone": "9123456789",
        "disease": "Fever",
        "address": "Hyderabad"
    }
    code, res = send_request("/patients/add/", "POST", pat1)
    print(f"POST /patients/add/ (Patient 1): Status {code}, Response: {res}")
    assert code == 201, f"Expected 201, got {code}"
    pat1_id = res['id']
    
    # 2. Add Patient 2
    pat2 = {
        "patient_name": "Sneha Patel",
        "age": 34,
        "gender": "Female",
        "phone": "9988776655",
        "disease": "Skin Allergy",
        "address": "Bangalore"
    }
    code, res = send_request("/patients/add/", "POST", pat2)
    print(f"POST /patients/add/ (Patient 2): Status {code}, Response: {res}")
    assert code == 201, f"Expected 201, got {code}"
    pat2_id = res['id']
    
    # 3. Get all Patients
    code, res = send_request("/patients/", "GET")
    print(f"GET /patients/: Status {code}, Total Patients: {len(res)}")
    assert code == 200, f"Expected 200, got {code}"
    
    # 4. Update Patient 1
    pat1_updated = pat1.copy()
    pat1_updated['age'] = 29
    code, res = send_request(f"/patients/update/{pat1_id}/", "PUT", pat1_updated)
    print(f"PUT /patients/update/{pat1_id}/: Status {code}, Response: {res}")
    assert code == 200, f"Expected 200, got {code}"
    assert res['age'] == 29
    
    # 5. Delete Patient 2
    code, res = send_request(f"/patients/delete/{pat2_id}/", "DELETE")
    print(f"DELETE /patients/delete/{pat2_id}/: Status {code}, Response: {res}")
    assert code == 200, f"Expected 200, got {code}"
    
    # 6. Verify Delete
    code, res = send_request("/patients/", "GET")
    print(f"GET /patients/ (after delete): Status {code}, Total Patients: {len(res)}")
    assert code == 200, f"Expected 200, got {code}"
    assert not any(p['id'] == pat2_id for p in res), "Patient 2 should have been deleted"

def test_appointments():
    print("\n--- Testing Appointment APIs ---")
    
    # 1. Add Appointment 1
    apt1 = {
        "patient_name": "Rahul Sharma",
        "doctor_name": "Dr. Ramesh Kumar",
        "appointment_date": "2026-07-20",
        "appointment_time": "10:30:00",
        "status": "Confirmed"
    }
    code, res = send_request("/appointments/add/", "POST", apt1)
    print(f"POST /appointments/add/ (Appointment 1): Status {code}, Response: {res}")
    assert code == 201, f"Expected 201, got {code}"
    apt1_id = res['id']
    
    # 2. Add Appointment 2
    apt2 = {
        "patient_name": "Sneha Patel",
        "doctor_name": "Dr. Priya Sharma",
        "appointment_date": "2026-07-21",
        "appointment_time": "02:00:00",
        "status": "Pending"
    }
    code, res = send_request("/appointments/add/", "POST", apt2)
    print(f"POST /appointments/add/ (Appointment 2): Status {code}, Response: {res}")
    assert code == 201, f"Expected 201, got {code}"
    apt2_id = res['id']
    
    # 3. Get all Appointments
    code, res = send_request("/appointments/", "GET")
    print(f"GET /appointments/: Status {code}, Total Appointments: {len(res)}")
    assert code == 200, f"Expected 200, got {code}"
    
    # 4. Update Appointment 1
    apt1_updated = apt1.copy()
    apt1_updated['status'] = "Cancelled"
    code, res = send_request(f"/appointments/update/{apt1_id}/", "PUT", apt1_updated)
    print(f"PUT /appointments/update/{apt1_id}/: Status {code}, Response: {res}")
    assert code == 200, f"Expected 200, got {code}"
    assert res['status'] == "Cancelled"
    
    # 5. Delete Appointment 2
    code, res = send_request(f"/appointments/delete/{apt2_id}/", "DELETE")
    print(f"DELETE /appointments/delete/{apt2_id}/: Status {code}, Response: {res}")
    assert code == 200, f"Expected 200, got {code}"
    
    # 6. Verify Delete
    code, res = send_request("/appointments/", "GET")
    print(f"GET /appointments/ (after delete): Status {code}, Total Appointments: {len(res)}")
    assert code == 200, f"Expected 200, got {code}"
    assert not any(a['id'] == apt2_id for a in res), "Appointment 2 should have been deleted"

if __name__ == "__main__":
    print("Waiting 2 seconds for server to ensure it is listening...")
    time.sleep(2)
    try:
        test_doctors()
        test_patients()
        test_appointments()
        print("\nAll 12 API tests passed successfully!")
    except AssertionError as e:
        print(f"\nAssertion error during API test execution: {e}")
    except Exception as e:
        print(f"\nUnexpected error during API test execution: {e}")
