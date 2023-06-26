from rest_framework import serializers
from .models import owners,pets , doctors, appointments, vaccines

class ownersSerializer(serializers.ModelSerializer):
    class Meta:
        model = owners
        fields = '__all__'
class petsSerializer(serializers.ModelSerializer):
    class Meta:
        model = pets
        fields = '__all__'

class doctorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = doctors
        fields = '__all__'

class appointmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = appointments
        fields = '__all__'
        