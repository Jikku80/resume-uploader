from django import forms
from .models import Resume

GENDER_CHOICES = [
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other')
]

JOB_CITY_CHOICES = [
    ('Lalitpur', 'Lalitpur'),
    ('Pokhara', 'Pokhara'),
    ('Janakpur', 'Janakpur'),
    ('Karnali', 'Karnali'),
    ('Biratnagar', 'Biratnagar'),
    ('Lumbini', 'Lumbini')
]


class ResumeForm(forms.ModelForm):
    gender = forms.ChoiceField(
        choices=GENDER_CHOICES, widget=forms.RadioSelect)
    job_city = forms.MultipleChoiceField(
        label='Preffered Location', choices=JOB_CITY_CHOICES, widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Resume
        fields = ['name', 'dob', 'gender', 'locality', 'city',
                  'pin', 'state', 'mobile', 'email', 'job_city', 'profile_image', 'my_file']
        labels = {
            'name': 'Full Name',
            'dob': 'Date of Birth',
            'pin': 'ZIP Code',
            'mobile': 'Mobile No.',
            'email': 'Email Id',
            'job_city': 'Work Place',
            'profile_image': 'Profile Pic',
            'my_file': 'Upload Document'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'dob': forms.DateInput(attrs={'class': 'form-control', 'id': 'datepicker'}),
            'locality': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'pin': forms.NumberInput(attrs={'class': 'form-control'}),
            'state': forms.Select(attrs={'class': 'form-control'}),
            'mobile': forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'})
        }
