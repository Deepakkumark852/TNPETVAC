from django.db import models
import phonenumber_field.modelfields as phonenumber

# Create your models here.
class owners(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone = phonenumber.PhoneNumberField(default='+91')
    email = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=200)
    pet_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)

class pets(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    species =(
        ('C','Canine'),
        ('F','Feline')
    )
    breed = models.CharField(max_length=200)
    age = models.IntegerField()
    owner_id = models.ForeignKey(owners, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    microchip = models.IntegerField()
    color = models.CharField(max_length=50)
    sex = (
        ('M','Male'),
        ('F','Female')
    )
    dob = models.DateField()

    def __str__(self):
        return str(self.id)
    

    
class vaccines(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    week_no = models.IntegerField()
    species =(
        ('C','Canine'),
        ('F','Feline')
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)
    
class doctors(models.Model):
    id = models.AutoField(primary_key=True)
    hospital_name = models.CharField(max_length=200)
    hospital_address = models.CharField(max_length=200)
    hospital_phone = phonenumber.PhoneNumberField(default='+91')
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)
    
class Invoices:
    id = models.AutoField(primary_key=True)
    appointment_id = models.IntegerField()

    def __str__(self):
        return str(self.id)
    
class appointments(models.Model):
    id = models.AutoField(primary_key=True)
    pet_id = models.ForeignKey(pets, on_delete=models.CASCADE)
    owner_id = models.ForeignKey(owners, on_delete=models.CASCADE)
    doctor_id = models.ForeignKey(doctors, on_delete=models.CASCADE)
    vaccine_id = models.ForeignKey(vaccines, on_delete=models.CASCADE)
    request_status =(
        ('P','Pending'),
        ('A','Approved'),
        ('R','Rejected')
    )
    date = models.DateField()
    time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)