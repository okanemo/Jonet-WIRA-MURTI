# PatientLab Endpoint

## Description

An endpoint to parse PatientLab data.

## Technology stack

1. Django
2. PostgreSQL

## Instruction 

1. create a user and a database in PostgreSQL

2. set DATABASES variable inside okenemo_test/settings.py

    ```
    NAME: set database name [string],
    USER: set database username [string],
    PASSWORD: set database password [string],
    HOST: set database host [string]
    ```

3. if using virtualenv :

    ```
    pip install virtualenv
    virtualenv venv
    ./venv/Scripts/activate
    ```

4. install requirements

    ```
    pip install -r requirements.txt
    ```

5. migrate database

    ```
    python manage.py migrate
    ```

6. run server

    ```
    python manage.py runserver
    ```

## Endpoint

1. create PatientLab data
    * URL
      /api/patientlab

    * Method
      POST
      
    * URL Params
      None
      
    * Data Params Case 1 (json)
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

    * Data Params Case 2 (json)
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
