from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ownersSerializer, petsSerializer , doctorsSerializer , appointmentsSerializer , vaccinesSerializer
from .models import owners, pets , doctors , appointments, vaccines
import geopy.distance
from django.contrib.auth.hashers import make_password, check_password
import jwt

@api_view(['GET'])
def apiOverview(request):
    routes = [
        {
        'Endpoint': '/owners/',
        'method': 'GET',
        'body': None,
        'description': 'Returns a list of all owners'
        },
        {
        'Endpoint': '/owners/<str:pk>/',
        'method': 'GET',
        'body': None,
        'description': 'Returns a single owner'
        },
        {
        'Endpoint': '/owners/create/',
        'method': 'POST',
        'body': {'name', 'address', 'phone', 'email', 'password', 'pet_id'},
        'description': 'Creates a new owner'
        },
        {
        'Endpoint': '/owners/update/<str:pk>/',
        'method': 'PUT',
        'body': {'name', 'address', 'phone', 'email', 'password', 'pet_id'},
        'description': 'Updates an owner'
        },
        {
        'Endpoint': '/owners/delete/<str:pk>/',
        'method': 'DELETE',
        'body': None,
        'description': 'Deletes an owner'
        },
        {
        'Endpoint': '/pets/',
        'method': 'GET',
        'body': None,
        'description': 'Returns a list of all pets'
        },
        {
        'Endpoint': '/pet/<str:pk>/',
        'method': 'GET',
        'body': None,
        'description': 'Returns a single pet'
        },
        {   
        'Endpoint': '/pets/create/',
        'method': 'POST',
        },
        {
        'Endpoint': '/pets/update/<str:pk>/',
        'method': 'PUT',
        },
        {
        'Endpoint': '/pets/delete/<str:pk>/',
        'method': 'DELETE',
        'body': None,
        'description': 'Deletes a pet'
        },
        {
        'Endpoint': '/doctorAuth/',
        'method': 'POST',
        'body': {'email', 'password'},
        'description': 'Returns a single doctor'
        },
        {
        'Endpoint': '/doctors/',
        'method': 'GET',
        'body': None,
        'description': 'Returns a list of all doctors'
        },
        {
        'Endpoint': '/doctor/<str:pk>/',    
        'method': 'GET',
        'body': None,
        'description': 'Returns a single doctor'
        },
        {
        'Endpoint': '/doctors/create/',
        'method': 'POST',
        'body': {'name', 'address', 'phone', 'email', 'password', 'hospital_address'},
        'description': 'Creates a new doctor'
        },
        {
        'Endpoint': '/doctors/update/<str:pk>/',
        'method': 'PUT',
        'body': {'name', 'address', 'phone', 'email', 'password', 'hospital_address'},
        'description': 'Updates a doctor'
        },
        {
        'Endpoint': '/doctors/delete/<str:pk>/',
        'method': 'DELETE',
        'body': None,
        'description': 'Deletes a doctor'
        },
        {
        'Endpoint': '/appointments/',
        'method': 'GET',
        'body': None,
        'description': 'Returns a list of all appointments'
        },
        {
        'Endpoint': '/appointment/<str:pk>/',
        'method': 'GET',
        'body': None,
        'description': 'Returns a single appointment'
        },
        {
        'Endpoint': '/appointments/create/',
        'method': 'POST',
        'body': {'pet_id', 'owner_id', 'doctor_id', 'vaccine_id', 'request_status', 'date', 'time'},
        'description': 'Creates a new appointment'
        },
        {
        'Endpoint': '/appointments/update/<str:pk>/',
        'method': 'PUT',
        'body': {'pet_id', 'owner_id', 'doctor_id', 'vaccine_id', 'request_status', 'date', 'time'},
        'description': 'Updates an appointment'
        },
        {
        'Endpoint': '/appointments/delete/<str:pk>/',
        'method': 'DELETE',
        'body': None,
        'description': 'Deletes an appointment'
        },
        {
        'Endpoint': '/appointmentdocotorlist/<str:doctor>/',
        'method': 'GET',
        'body': None,
        'description': 'Returns a list of all appointments by doctor'
        },
        {
        'Endpoint': '/appointmentpetlist/<str:pet>/',
        'method': 'GET',
        'body': None,
        'description': 'Returns a list of all appointments by pet'
        },
        {
        'Endpoint': '/appointmentownerlist/<str:owner>/',
        'method': 'GET',
        'body': None,
        'description': 'Returns a list of all appointments by owner'
        },
        {
        'Endpoint': '/appointmentdoctorpet/<str:doctor>/<str:pet>/',
        'method': 'GET',
        'body': None,
        'description': 'Returns a list of all appointments by doctor and pet'
        },
        {
        'Endpoint': '/appointmentdoctorowner/<str:doctor>/<str:owner>/',
        'method': 'GET',
        'body': None,
        'description': 'Returns a list of all appointments by doctor and owner'
        },
        {
        'Endpoint': '/appointmentpetowner/<str:pet>/<str:owner>/',
        'method': 'GET',
        'body': None,
        'description': 'Returns a list of all appointments by pet and owner'
        },
        {
        'Endpoint': '/appointmentpetownerdoctor/<str:doctor>/<str:pet>/<str:owner>',
        'method': 'GET',
        'body': None,
        'description': 'Returns a list of all appointments by doctor, pet and owner'
        },
        {
        'Endpoint': '/appointmentowner/<str:owner>/',
        'method': 'GET',
        'body': None,
        'description': 'Returns a list of all appointments by owner'
        },
        {
        'Endpoint': '/appointmentdoctor/<str:doctor>/',
        'method': 'GET',
        'body': None,
        'description': 'Returns a list of all appointments by doctor'
        },
        {
        'Endpoint': '/appointmentpet/<str:pet>/',
        'method': 'GET',
        'body': None,
        'description': 'Returns a list of all appointments by pet'
        },
        {
        'Endpoint': '/appointmentdate/<str:date>/',
        'method': 'GET',
        'body': None,
        'description': 'Returns a list of all appointments by date'
        },
        {
        'Endpoint': '/appointmentdateequal/<str:date>/',
        'method': 'GET',
        'body': None,
        'description': 'Returns a list of all appointments by date'
        },
        {
        'Endpoint': '/vaccines/',
        'method': 'GET',
        'body': None,
        'description': 'Returns a list of all vaccines'
        },
        {
        'Endpoint': '/vaccine/<str:pk>/',
        'method': 'GET',
        'body': None,
        'description': 'Returns a single vaccine'
        },
        {
        'Endpoint': '/vaccines/create/',
        'method': 'POST',
        'body': {'name', 'description', 'week_no'},
        'description': 'Creates a new vaccine'
        },
        {
        'Endpoint': '/vaccines/update/<str:pk>/',
        'method': 'PUT',
        'body': {'name', 'description', 'week_no'},
        'description': 'Updates a vaccine'
        },
        {
        'Endpoint': '/vaccines/delete/<str:pk>/',
        'method': 'DELETE',
        'body': None,
        'description': 'Deletes a vaccine'
        }
    ]
    return Response(routes)



###################### owners api views ######################

@api_view(['GET'])
def ownersList(request):
    own = owners.objects.all()
    serializer = ownersSerializer(own, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def ownerDetail(request, pk):   
    own = owners.objects.get(id=pk)
    serializer = ownersSerializer(own, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def ownerAuth(request):
    own = owners.objects.get(email=request.data['email'])
    if check_password(request.data['password'], own.password):
        serializer = ownersSerializer(own, many=False)
        token = jwt.encode(serializer.data,key='secret',algorithm='HS256')
        return Response(token)
    else:
        return Response(serializer.errors)

@api_view(['POST'])
def ownerCreate(request):
    datar = request.data.copy()
    datar['password'] = make_password(datar['password'])
    serializer = ownersSerializer(data=datar)
    if serializer.is_valid():
        serializer.save()
    if serializer.errors:
        return Response(serializer.errors)
    return Response(serializer.data)

@api_view(['PUT'])
def ownerUpdate(request, pk):
    own = owners.objects.get(id=pk)
    serializer = ownersSerializer(instance=own, data=request.data)
    if serializer.is_valid():
        serializer.save()
    if serializer.errors:
        return Response(serializer.errors)
    return Response(serializer.data)

@api_view(['DELETE'])
def ownerDelete(request, pk):
    own = owners.objects.get(id=pk)
    own.delete()
    return Response('Owner deleted')


######################################## pets api views   ###############################################
@api_view(['GET'])
def petsList(request):
    pet = pets.objects.all()
    serializer = petsSerializer(pet, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def petDetail(request, pk):
    pet = pets.objects.get(id=pk)
    serializer = petsSerializer(pet, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def petCreate(request):
    serializer = petsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    if serializer.errors:
        return Response(serializer.errors)
    return Response(serializer.data)

@api_view(['PUT'])
def petUpdate(request, pk):
    pet = pets.objects.get(id=pk)
    serializer = petsSerializer(instance=pet, data=request.data)
    if serializer.is_valid():
        serializer.save()
    if serializer.errors:
        return Response(serializer.errors)
    return Response(serializer.data)

@api_view(['DELETE'])
def petDelete(request, pk):
    if request.method == 'DELETE':
        pet = pets.objects.get(id=pk)
        pet.delete()
        pet.save()
        return Response('Pet deleted')

@api_view(['GET'])
def petOwner(request, pk):
    pet = pets.objects.get(id=pk)
    own = owners.objects.get(id=pet.owner_id)
    serializer = ownersSerializer(own, many=False)
    return Response(serializer.data)


######################################## doctor api views   ###############################################

@api_view(['GET'])
def doctorList(request):
    doc = doctors.objects.all()
    serializer = doctorsSerializer(doc, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def doctorDetail(request, pk):
    doc = doctors.objects.get(id=pk)
    serializer = doctorsSerializer(doc, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def doctorAuth(request):
    doc = doctors.objects.get(email=request.data['email'], password=request.data['password'])
    serializer = doctorsSerializer(doc, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def doctorCreate(request):
    serializer = doctorsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.data['password'] = make_password(serializer.data['password'])
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
def doctorUpdate(request, pk):
    doc = doctors.objects.get(id=pk)
    serializer = doctorsSerializer(instance=doc, data=request.data)
    if serializer.is_valid():
        serializer.save()
    if serializer.errors:
        return Response(serializer.errors)
    return Response(serializer.data)

@api_view(['DELETE'])
def doctorDelete(request, pk):
    doc = doctors.objects.get(id=pk)
    doc.delete()
    return Response('Doctor deleted')

@api_view(['GET'])
def getDoctor(request,lat,lng):
    doc = doctors.objects.all()
    doc1 = []
    for eachdoc in doc : 
        coords_1 = (float(lat), float(lng))
        coords_2 = tuple(float(num)  for num in eachdoc.hospital_address.strip('()').split(','))
        if geopy.distance.geodesic(coords_1, coords_2).km < 20:
            doc1.append(eachdoc.id)
    doc = doctors.objects.filter(id__in=doc1)

    serializer = doctorsSerializer(doc, many=True)
    return Response(serializer.data)

######################################## appointment api views   ###############################################

@api_view(['GET'])
def appointmentList(request):
    app = appointments.objects.all()
    serializer = appointmentsSerializer(app, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def appointmentDetail(request, pk):
    app = appointments.objects.get(id=pk)
    serializer = appointmentsSerializer(app, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def appointmentCreate(request):
    serializer = appointmentsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    if serializer.errors:
        return Response(serializer.errors)
    return Response(serializer.data)

@api_view(['PUT'])
def appointmentUpdate(request, pk):
    app = appointments.objects.get(id=pk)
    serializer = appointmentsSerializer(instance=app, data=request.data)
    if serializer.is_valid():
        serializer.save()
    if serializer.errors:
        return Response(serializer.errors)
    return Response(serializer.data)

@api_view(['DELETE'])
def appointmentDelete(request, pk):
    app = appointments.objects.get(id=pk)
    app.delete()
    return Response('Appointment deleted')

######################################## pet, owner, doctor by appointment api views   ###############################################

@api_view(['GET'])
def appointmentDoctor(request, pk):
    app = appointments.objects.get(id=pk)
    doc = doctors.objects.get(id=app.doctor_id)
    serializer = doctorsSerializer(doc, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def appointmentPet(request, pk):
    app = appointments.objects.get(id=pk)
    pet = pets.objects.get(id=app.pet_id)
    serializer = petsSerializer(pet, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def appointmentOwner(request, pk):
    app = appointments.objects.get(id=pk)
    pet = pets.objects.get(id=app.pet_id)
    own = owners.objects.get(id=pet.owner_id)
    serializer = ownersSerializer(own, many=False)
    return Response(serializer.data)

######################################## appointment by pet, owner, doctor api views   ###############################################

@api_view(['GET'])
def appointmentDoctorList(request, pk):
    app = appointments.objects.filter(doctor_id=pk)
    serializer = appointmentsSerializer(app, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def appointmentPetList(request, pk):
    app = appointments.objects.filter(pet_id=pk)
    serializer = appointmentsSerializer(app, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def appointmentOwnerList(request, pk):
    app = appointments.objects.filter(pet_id=pk)
    serializer = appointmentsSerializer(app, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def appointmentDoctorPet(request, pk, pk2):
    app = appointments.objects.filter(doctor_id=pk, pet_id=pk2)
    serializer = appointmentsSerializer(app, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def appointmentDoctorOwner(request, pk, pk2):
    app = appointments.objects.filter(doctor_id=pk)
    serializer = appointmentsSerializer(app, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def appointmentPetOwner(request, pk, pk2):
    app = appointments.objects.filter(pet_id=pk, owner_id=pk2)
    serializer = appointmentsSerializer(app, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def appointmentDoctorPetOwner(request, pk, pk2, pk3):
    app = appointments.objects.filter(doctor_id=pk, pet_id=pk2, owner_id=pk3)
    serializer = appointmentsSerializer(app, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def appointmentDoctorPetOwnerDate(request, pk, pk2, pk3, pk4):
    app = appointments.objects.filter(doctor_id=pk, pet_id=pk2, owner_id=pk3, date=pk4)
    serializer = appointmentsSerializer(app, many=True)
    return Response(serializer.data)

######################################## appointment by date api views   ###############################################

@api_view(['GET'])
def appointmentdate(request, pk):
    app = appointments.objects.filter(date__gte=pk)
    serializer = appointmentsSerializer(app, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def appointmentdateequal(request, pk):
    app = appointments.objects.filter(date=pk)
    serializer = appointmentsSerializer(app, many=True)
    return Response(serializer.data)

######################################## vaccines api views   ###############################################

@api_view(['GET'])
def vaccineList(request):
    vac = vaccines.objects.all()
    serializer = vaccinesSerializer(vac, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def vaccineDetail(request, pk):
    vac = vaccines.objects.get(id=pk)
    serializer = vaccinesSerializer(vac, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def vaccineCreate(request):
    serializer = vaccinesSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    if serializer.errors:
        return Response(serializer.errors)
    return Response(serializer.data)

@api_view(['PUT'])
def vaccineUpdate(request, pk):
    vac = vaccines.objects.get(id=pk)
    serializer = vaccinesSerializer(instance=vac, data=request.data)
    if serializer.is_valid():
        serializer.save()
    if serializer.errors:
        return Response(serializer.errors)
    return Response(serializer.data)

@api_view(['DELETE'])
def vaccineDelete(request, pk):
    vac = vaccines.objects.get(id=pk)
    vac.delete()
    return Response('Vaccine deleted')

@api_view(['GET'])
def vaccinePet(request, pk):
    vac = vaccines.objects.get(id=pk)
    pet = pets.objects.get(id=vac.pet_id)
    serializer = petsSerializer(pet, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def vaccineOwner(request, pk):
    vac = vaccines.objects.get(id=pk)
    pet = pets.objects.get(id=vac.pet_id)
    own = owners.objects.get(id=pet.owner_id)
    serializer = ownersSerializer(own, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def vaccinePetList(request, pk):
    vac = vaccines.objects.filter(pet_id=pk)
    serializer = vaccinesSerializer(vac, many=True)
    return Response(serializer.data)
