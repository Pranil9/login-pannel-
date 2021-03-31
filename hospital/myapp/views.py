from django.contrib import messages
from django.shortcuts import render, redirect
from myapp.models import Patient
from django.http import HttpResponseRedirect
from myapp.forms import PatientForm
from myapp.models import Appointment
from myapp.forms import AppointmentForm



# Create your views here.
def create(request):
    if request.method=="POST":
        form=PatientForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
        else:
            messages.error(request,"fill the form properly")
    else:
        form=PatientForm()
    return render(request,'index.html' , {'form':form})

def show(request):
    patient1 = Patient.objects.all()
    return render(request, 'show.html', {'patient1':patient1})

def edit(request,id):
    employee = Patient.objects.get(id=id)
    return render(request,'edit.html',{'patient1':employee})

def update(request, id):
    employee = Patient.objects.get(id=id)
    form = PatientForm(request.POST, instance = employee)
    if form.is_valid():
        form.save()
        return redirect('/show')
    else:
        messages.error(request, "fill the form properly")
    return render(request, 'edit.html', {'patient1': employee})

def destroy(request, id):
    patient2 = Patient.objects.get(id=id)
    patient2.delete()
    patient1=Patient.objects.all()
    return render(request,'show.html',{'patient1': patient1})


def capp(request):
    if request.method=="POST":
        form=AppointmentForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/Show_appointment')
            except:
                pass
        else:
            messages.error(request, "fill the form properly")
    else:
        form=AppointmentForm()
    return render(request,'apmta.html' , {'form':form})

def sapp(request):
    patient1 = Appointment.objects.all()
    return render(request, 'apmtb.html', {'patient1':patient1})

def cancel(request, id):
    patient2 = Appointment.objects.get(id=id)
    patient2.delete()
    patient1=Appointment.objects.all()
    return render(request,'apmtb.html',{'patient1': patient1})

def change(request,id):
    employee = Appointment.objects.get(id=id)
    return render(request,'change.html',{'patient1':employee})

def updatee(request, id):
    employee = Appointment.objects.get(id=id)
    form = AppointmentForm(request.POST, instance = employee)
    if form.is_valid():
        form.save()
        return redirect('/Show_appointment')
    else:
        messages.error(request, "fill the form properly")
    return render(request, 'change.html', {'patient1': employee})

def home(request):
    return render(request, 'login.html')

def doctor(request):
    return render(request, 'optiondoc.html')

def appointment(request):
    patient1 = Appointment.objects.all()
    return render(request, 'showap.html',{'patient1':patient1} )

def todays(request):
    patient1=Patient.objects.all()
    return render(request, 'showd.html' ,{'patient1':patient1})

