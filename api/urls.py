from django.urls import path, include

urlpatterns = [
    path('patientlab/', include('api.patientlab.urls')),
]