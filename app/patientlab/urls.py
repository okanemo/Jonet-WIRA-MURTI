from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_patientlab, name='create_patientlab'),
]