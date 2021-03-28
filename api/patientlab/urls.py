from django.urls import path
from . import controller

urlpatterns = [
    path('', controller.patient_lab_post, name='patient_lab_post'),
]