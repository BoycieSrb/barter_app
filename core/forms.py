from django import forms
from django.contrib.auth.models import User

class RegistrationForm(forms.Form):
    first_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-lg',
            'placeholder': 'Ime'
        })
    )
    last_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-lg',
            'placeholder': 'Prezime'
        })
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control form-control-lg',
            'placeholder': 'vas@email.com'
        })
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # PROVJERI DA LI POSTOJI PRED customizovanjem
        if 'password1' in self.fields:
            self.fields['password1'].label = 'Lozinka'
            self.fields['password1'].widget.attrs.update({
                'class': 'form-control form-control-lg',
                'placeholder': 'Unesite lozinku'
            })
        if 'password2' in self.fields:
            self.fields['password2'].label = 'Potvrdi lozinku'
            self.fields['password2'].widget.attrs.update({
                'class': 'form-control form-control-lg',
                'placeholder': 'Ponovite lozinku'
            })

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Korisnik sa ovim email-om već postoji!')
        return email

    def signup(self, request, user):
        """OBAVEZNA metoda za allauth."""
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.save()
        return user
