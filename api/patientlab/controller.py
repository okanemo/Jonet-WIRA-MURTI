from django.http import JsonResponse
from api.models import PatientLab
import json

def patient_lab_post(request):
    if request.method != 'POST':
        return JsonResponse({
            'error': 'Method Not Allowed'
        }, status=405)

    request_json = json.loads(request.body)

    to_be_added = parse(request_json)

    if not to_be_added:
        return JsonResponse({
            'error': 'Not Acceptable'
        }, status=406)

    try:
        patient_lab = PatientLab.objects.create(
            id_number = to_be_added['id_number'], 
            patient_name = to_be_added['patient_name'], 
            phone_mobile = None if 'phone_mobile' not in to_be_added else to_be_added['phone_mobile'],
            gender = to_be_added['gender'], 
            date_of_birth = to_be_added['date_of_birth'], 
            date_of_test = to_be_added['date_of_test'], 
            lab_number = to_be_added['lab_number'], 
            clinic_code = to_be_added['clinic_code'], 
            code = to_be_added['code'], 
            name = to_be_added['name'], 
            value = to_be_added['value'], 
            unit = to_be_added['unit'], 
            ref_range = to_be_added['ref_range'], 
            finding = to_be_added['finding'], 
            result_state = to_be_added['result_state']
        )

        return JsonResponse({
            'message': 'Created'
        }, status=201)
    except:
        return JsonResponse({
            'error': 'Conflict'
        }, status=409)

def parse(request_json):
    if ('patient_data' not in request_json):
        return case_1_parse(request_json)
    else:
        return case_2_parse(request_json)

def case_1_parse(request_json):
    to_be_added = {}

    if isCase1Valid(request_json):
        to_be_added['id_number'] = request_json['id_number']
        to_be_added['patient_name'] = request_json['patient_name']
        to_be_added['gender'] = request_json['gender']
        to_be_added['date_of_birth'] = request_json['date_of_birth']
        to_be_added['date_of_test'] = request_json['date_of_test']
        to_be_added['lab_number'] = request_json['lab_number']
        to_be_added['clinic_code'] = request_json['clinic_code']
        to_be_added['code'] = request_json['lab_studies'][0]['code']
        to_be_added['name'] = request_json['lab_studies'][0]['name']
        to_be_added['value'] = request_json['lab_studies'][0]['value']
        to_be_added['unit'] = request_json['lab_studies'][0]['unit']
        to_be_added['ref_range'] = request_json['lab_studies'][0]['ref_range']
        to_be_added['finding'] = request_json['lab_studies'][0]['finding']
        to_be_added['result_state'] = request_json['lab_studies'][0]['result_state']

    return to_be_added

def case_2_parse(request_json):
    to_be_added = {}

    if isCase2Valid(request_json):
        to_be_added['id_number'] = request_json['patient_data']['id_number']
        to_be_added['patient_name'] = ' '.join([request_json['patient_data']['first_name'], request_json['patient_data']['last_name']])
        to_be_added['phone_mobile'] = request_json['patient_data']['phone_mobile']
        to_be_added['gender'] = request_json['patient_data']['gender']
        to_be_added['date_of_birth'] = request_json['patient_data']['date_of_birth']
        to_be_added['date_of_test'] = request_json['date_of_test']
        to_be_added['lab_number'] = request_json['lab_number']
        to_be_added['clinic_code'] = request_json['clinic_code']
        to_be_added['code'] = request_json['lab_studies'][0]['code']
        to_be_added['name'] = request_json['lab_studies'][0]['name']
        to_be_added['value'] = request_json['lab_studies'][0]['value']
        to_be_added['unit'] = request_json['lab_studies'][0]['unit']
        to_be_added['ref_range'] = request_json['lab_studies'][0]['ref_range']
        to_be_added['finding'] = request_json['lab_studies'][0]['finding']
        to_be_added['result_state'] = request_json['lab_studies'][0]['result_state']

    return to_be_added

def isCase1Valid(request_json):
    request_json_check = (
        'id_number' in request_json,
        'patient_name' in request_json,
        'gender' in request_json,
        'date_of_birth' in request_json,
        'date_of_test' in request_json,
        'lab_number' in request_json,
        'clinic_code' in request_json
    )

    lab_stds_check = 'lab_studies' in request_json

    lab_stds_elmt_check = False if not lab_stds_check else (
        'code' in request_json['lab_studies'][0],
        'name' in request_json['lab_studies'][0],
        'value' in request_json['lab_studies'][0],
        'unit' in request_json['lab_studies'][0],
        'ref_range' in request_json['lab_studies'][0],
        'finding' in request_json['lab_studies'][0],
        'result_state' in request_json['lab_studies'][0]
    )

    return request_json_check and lab_stds_elmt_check

def isCase2Valid(request_json):
    patient_data_check = 'patient_data' in request_json

    patient_data_elmt_check = False if not patient_data_check else (
        'id_number' in request_json['patient_data']['id_number'],
        'first_name' in request_json['patient_data']['first_name'],
        'last_name' in request_json['patient_data']['last_name'],
        'phone_mobile' in request_json['patient_data']['phone_mobile'],
        'gender' in request_json['patient_data']['gender'],
        'date_of_birth' in request_json['patient_data']['date_of_birth']
    )

    request_json_check = (
        'date_of_test' in request_json,
        'lab_number' in request_json,
        'clinic_code' in request_json
    )

    lab_stds_check = 'lab_studies' in request_json

    lab_stds_elmt_check = False if not lab_stds_check else (
        'code' in request_json['lab_studies'][0],
        'name' in request_json['lab_studies'][0],
        'value' in request_json['lab_studies'][0],
        'unit' in request_json['lab_studies'][0],
        'ref_range' in request_json['lab_studies'][0],
        'finding' in request_json['lab_studies'][0],
        'result_state' in request_json['lab_studies'][0]
    )
    
    return patient_data_elmt_check and request_json_check and lab_stds_elmt_check