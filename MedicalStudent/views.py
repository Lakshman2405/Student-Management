from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Student
from .forms import StudentForm



def manage_view(request):
    if request.method=='POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save();
            return redirect('MedicalStudent:manage')
    else:
        form=StudentForm()
        students=Student.objects.all()
        return render(request,'manage.html',{'form':form ,'students':students})
    

def edit_view(request,reg_num):
    student=get_object_or_404(Student, pk=reg_num)
    if request.method=='POST':
        form=StudentForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
            return HttpResponse("Your data is updated")
    else:
        form=StudentForm(instance=student)
        return render(request,'edit.html',{'form':form})
    
def delete_view(request,reg_num):
    student=get_object_or_404(Student,pk=reg_num)
    if request.method=='POST':
        student.delete()
        return HttpResponse("<h2> Record Deleted Successfully </h2>")
    return render(request,'delete.html',{'student':student})







