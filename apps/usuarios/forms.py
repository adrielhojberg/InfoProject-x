from django import forms
from .models import Usuario
from django.contrib.auth.forms import UserCreationForm
from apps.perfil.models import Profile

def rubros():
    RUBRO1 = "OTROS"
    RUBRO2 = "HERRERO"
    RUBRO3 = "CARPINTERO"
    RUBRO_CHOICES = (
        (RUBRO3, "Carpintero"),
        (RUBRO2, "Herrero"),
        (RUBRO1, "Otros"),
    )      
    return RUBRO_CHOICES


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = Usuario
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = Usuario
        fields = ['username', 'email']
        widgets = {
                'username': forms.TextInput(attrs={'class': 'form-control'}),
                'email': forms.TextInput(attrs={'class': 'form-control'}),
            }
    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'email']:
            self.fields[fieldname].help_text = None
            self.fields[fieldname].label = ''

class ProfileUpdateForm(forms.ModelForm):
    rubro = forms.ChoiceField(choices=rubros())
    class Meta:
        model = Profile
        fields = ['image','aboutus','instagram','twitter','telefono','rubro']
        widgets = {
                'image':forms.FileInput(attrs={'class':'btn btn-primary mb-4'}),
                'instagram': forms.TextInput(attrs={'class': 'form-control mb-4'}),
                'aboutus': forms.TextInput(attrs={'class': 'form-control mb-4'}),
                'twitter': forms.TextInput(attrs={'class': 'form-control mb-4'}),
                'telefono': forms.TextInput(attrs={'class': 'form-control mb-4'}),

            }
    def __init__(self, *args, **kwargs):
        super(ProfileUpdateForm, self).__init__(*args, **kwargs)
        for fieldname in ['image','aboutus','instagram','twitter','telefono','rubro']:
            self.fields[fieldname].help_text = None
            self.fields[fieldname].label = ''