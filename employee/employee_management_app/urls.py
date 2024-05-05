from django.urls import path
from .views import EmployeeDetails

urlpatterns = [
    path('employee/<int:employee_id>/<str:dob>/', EmployeeDetails.as_view(), name='employee_details'),
    # Add more URLs as needed
]
