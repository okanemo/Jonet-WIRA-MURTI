from .libs import parser
from django.http import JsonResponse
from .models import PatientLab
from django.views.decorators.http import require_http_methods
import json

@require_http_methods(['POST'])
def create_patientlab(request):
    try:
        request_json = json.loads(request.body)
    except:
        return JsonResponse({
            'error': 'Request body should be in json format'
        }, status=400)

    to_be_added = parser.parse(request_json)

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