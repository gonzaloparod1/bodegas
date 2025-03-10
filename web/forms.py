# aquí van nuestros Formularios
from django.contrib.auth.forms import UserCreationForm
from django import forms # type: ignore
from .models import ContactForm, TipoBodega
from django.contrib.auth.models import User

#TODO_ REGISTER - FORM

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Requerido. Ingrese una dirección de correo electrónico válida.')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este correo electrónico ya está en uso.")
        return email


#___________________________________________________________________________________________________
#███████████████████████████████████████████████████████████████████████████████████████████████████

#TODO_ EDIT PROFILE -FORM
#* -> UserProfileForm - este form nos va a servir además para cuando vayamos a editar el perfil
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

        
#___________________________________________________________________________________________________
#███████████████████████████████████████████████████████████████████████████████████████████████████


#TODO__ FORM CONTACTO
class ContactModelForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['customer_email', 'customer_name', 'message']
        

#___________________________________________________________________________________________________
#███████████████████████████████████████████████████████████████████████████████████████████████████


#* Form que ya valida y entrega la info requerida (solo de ejemplo ya que no lo voy a usar)
class CotizacionForm(forms.Form):
    tipo_bodega = forms.ModelChoiceField(
        queryset=TipoBodega.objects.filter(bodegas__disponible=True).distinct(),
        label="Seleccionar tipo de bodega",
        empty_label="Seleccione un tipo de bodega"
    )