from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .models import Doctor, Patient, Appointment
from .forms import DoctorRegistrationForm, PatientRegistrationForm, AppointmentForm

def register_doctor(request):
    if request.method == 'POST':
        form = DoctorRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_doctor = True
            user.save()
            Doctor.objects.create(user=user)
            return redirect('login')
    else:
        form = DoctorRegistrationForm()
    return render(request, 'registration.html', {'form': form})

def register_patient(request):
    if request.method == 'POST':
        form = PatientRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_patient = True
            user.save()
            Patient.objects.create(user=user)
            return redirect('login')
    else:
        form = PatientRegistrationForm()
    return render(request, 'registration.html', {'form': form})

@login_required
def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.patient = request.user.patient
            appointment.save()
            return redirect('appointments')
    else:
        form = AppointmentForm()
    return render(request, 'appointment.html', {'form': form})

@login_required
def view_doctors(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctor_list.html', {'doctors': doctors})

@login_required
def view_patients(request):
    if request.user.is_doctor:
        patients = Patient.objects.filter(appointment__doctor=request.user.doctor)
        return render(request, 'patient_list.html', {'patients': patients})
    return redirect('home')

@login_required
def profile(request):
    return render(request, 'profile.html')
