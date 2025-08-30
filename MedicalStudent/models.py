from django.db import models

# Create your models here.
class Student(models.Model):
    PROGRAM_LIST=[('MBBS','MBBS'),('MD','MD')]
    FEE_STATUS=[('PAID','Paid'),('NOT','Not Paid')]
    StudentRegNumber=models.CharField(max_length=50,unique=True,primary_key=True)
    StudentName=models.CharField(max_length=100,unique=True)
    NameOfTheProgramme=models.CharField(max_length=10,choices=PROGRAM_LIST)
    StudentAddress=models.TextField()
    ContactMobileNumber=models.CharField(max_length=10)
    StatusOftheSemesterFee=models.CharField(max_length=10,choices=FEE_STATUS,default='NOT')

    def __str__(self):
        return f"{self.StudentRegNumber}-{self.StudentName}"
    

