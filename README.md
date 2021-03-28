# PatientLab Endpoint

## Description

An endpoint to parse PatientLab data.

## Technology stack

1. Django
2. PostgreSQL

## Instruction 

1. to run the program :

    ```
    docker-compose build
    docker-compose up
    ```

## Endpoint

1. create PatientLab data
    * URL :
      /api/v1/patientlab

    * Method :
      POST
      
    * URL Params :
      None
      
    * Body Case 1 (json)
    ```
    { 
        "date_of_test":[string], 
        "id_number":[string], 
        "patient_name":[string]4", 
        "gender":[string], 
        "date_of_birth":[string], 
        "lab_number":[string]1-124", 
        "clinic_code":[string], 
        "lab_studies":[
            {
            "code":[string], 
            "name":[string], 
            "value":[string], 
            "unit":[string], 
            "ref_range":[string], 
            "finding":[string], 
            "result_state":[string]
            } 
        ]
    }
    ```

    * Body Case 2 (json)
    ```
    { 
        "patient_data":
        {
            "id_number":[string], 
            "first_name":[string], 
            "last_name":[string], 
            "phone_mobile":"[string]" 
            "gender":[string], 
            "date_of_birth":[string],
        }, 
        "date_of_test":[string], 
        "lab_number":[string], 
        "clinic_code":[string], 
        "lab_studies":[
            {
                "code":[string], 
                "name":[string], 
                "value":[string], 
                "unit":[string], 
                "ref_range":[string], 
                "finding":[string], 
                "result_state":[string]
            } 
        ]
    }
    ```
