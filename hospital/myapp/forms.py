from django import forms
from myapp.models import Patient
from myapp.models import Appointment




class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields="__all__"


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields="__all__"


