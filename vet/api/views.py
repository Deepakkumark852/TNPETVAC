from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ownersSerializer, petsSerializer , doctorsSerializer , appointmentsSerializer 
from .models import owners, pets , doctors , appointments


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
def ownerCreate(request):
    serializer = ownersSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
def ownerUpdate(request, pk):
    own = owners.objects.get(id=pk)
    serializer = ownersSerializer(instance=own, data=request.data)
    if serializer.is_valid():
        serializer.save()
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
    return Response(serializer.data)

@api_view(['PUT'])
def petUpdate(request, pk):
    pet = pets.objects.get(id=pk)
    serializer = petsSerializer(instance=pet, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def petDelete(request, pk):
    pet = pets.objects.get(id=pk)
    pet.delete()
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
def doctorCreate(request):
    serializer = doctorsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
def doctorUpdate(request, pk):
    doc = doctors.objects.get(id=pk)
    serializer = doctorsSerializer(instance=doc, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def doctorDelete(request, pk):
    doc = doctors.objects.get(id=pk)
    doc.delete()
    return Response('Doctor deleted')

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
    return Response(serializer.data)

@api_view(['PUT'])
def appointmentUpdate(request, pk):
    app = appointments.objects.get(id=pk)
    serializer = appointmentsSerializer(instance=app, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def appointmentDelete(request, pk):
    app = appointments.objects.get(id=pk)
    app.delete()
    return Response('Appointment deleted')

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

@api_view(['GET'])
def appointmentDoctorPetOwnerDateStart(request, pk, pk2, pk3, pk4, pk5):
    app = appointments.objects.filter(doctor_id=pk, pet_id=pk2, owner_id=pk3, date=pk4, start=pk5)
    serializer = appointmentsSerializer(app, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def appointmentDoctorPetOwnerDateStartEnd(request, pk, pk2, pk3, pk4, pk5, pk6):
    app = appointments.objects.filter(doctor_id=pk, pet_id=pk2, owner_id=pk3, date=pk4, start=pk5, end=pk6)
    serializer = appointmentsSerializer(app, many=True)
    return Response(serializer.data)

######################################## vaccines api views   ###############################################
