from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview),
    # owners
    path('ownerAuth/', views.ownerAuth),
    path('owners/', views.ownersList),
    path('owner/<str:pk>/', views.ownerDetail),
    path('owners/create/', views.ownerCreate),
    path('owners/update/<str:pk>/', views.ownerUpdate),
    path('owners/delete/<str:pk>/', views.ownerDelete),
    # pets
    path('pets/', views.petsList),
    path('petsbyowner/<str:pk>/', views.petsListOwner),
    path('pet/<str:pk>/', views.petDetail),
    path('pets/create/', views.petCreate),
    path('pets/update/<str:pk>/', views.petUpdate),
    path('pets/delete/<str:pk>/', views.petDelete),
    # doctors
    path('doctorAuth/', views.doctorAuth),
    path('getdoctor/<str:lat>/<str:lng>/', views.getDoctor),
    path('doctors/', views.doctorList),
    path('doctor/<str:pk>/', views.doctorDetail),
    path('doctors/create/', views.doctorCreate),
    path('doctors/update/<str:pk>/', views.doctorUpdate),
    path('doctors/delete/<str:pk>/', views.doctorDelete),
    # appointments
    path('appointments/', views.appointmentList),
    path('appointment/<str:pk>/', views.appointmentDetail),
    path('appointments/create/', views.appointmentCreate),
    path('appointments/update/<str:pk>/', views.appointmentUpdate),
    path('appointments/delete/<str:pk>/', views.appointmentDelete),
    # appointments by pet, owner, doctor
    path('appointmentdocotorlist/<str:doctor>/', views.appointmentDoctorList),
    path('appointmentpetlist/<str:pet>/', views.appointmentPetList),
    path('appointmentownerlist/<str:owner>/', views.appointmentOwnerList),
    path('appointmentdoctorpet/<str:doctor>/<str:pet>/', views.appointmentDoctorPet),
    path('appointmentdoctorowner/<str:doctor>/<str:owner>/', views.appointmentDoctorOwner),
    path('appointmentpetowner/<str:pet>/<str:owner>/', views.appointmentPetOwner),
    path('appointmentpetownerdoctor/<str:doctor>/<str:pet>/<str:owner>', views.appointmentDoctorPetOwner),
     # pet,owner,doctor by appointment
    path('appointmentowner/<str:owner>/', views.appointmentOwner),
    path('appointmentdoctor/<str:doctor>/', views.appointmentDoctor),
    path('appointmentpet/<str:pet>/', views.appointmentPet),
    # appointments by date
    path('appointmentdate/<str:date>/', views.appointmentdate),
    path('appointmentdateequal/<str:date>/', views.appointmentdateequal),
    #vaccines
    path('vaccines/', views.vaccineList),
    path('vaccine/<str:pk>/', views.vaccineDetail),
    path('vaccines/create/', views.vaccineCreate),
    path('vaccines/update/<str:pk>/', views.vaccineUpdate),
    path('vaccines/delete/<str:pk>/', views.vaccineDelete),

]