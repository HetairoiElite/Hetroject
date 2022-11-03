# forms

from django import forms

from hetapp.models import Tipo_usuario


class TUsuarioForm(forms.Form):
    username = forms.CharField(max_length=100, label="")
    password = forms.CharField(
        max_length=100, label="", widget=forms.PasswordInput())
    # custom label with css
    recuerdame = forms.BooleanField(required=False, label="Recordar")

    def __init__(self, *args, **kwargs):
        super(TUsuarioForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Usuario'})
        self.fields['password'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Contraseña'})


# Tipo_usuarios = Tipo_usuario.objects.filter(
#     pk__in=['1', "3"]).values_list("id_tipo_usuario", "nombre")

# print(Tipo_usuarios)


class TUsuarioCreateForm(forms.Form):

    username = forms.CharField(max_length=100, label="")
    correo = forms.EmailField(max_length=100, label="Correo")
    nombre = forms.CharField(max_length=100, label="Nombre")
    apellidoP = forms.CharField(max_length=100, label="Apellido paterno")
    apellidoM = forms.CharField(max_length=100, label="Apellido materno")
    # tipo_usuarios = forms.ChoiceField(
    #     widget=forms.Select, choices=Tipo_usuarios, label="Tipo de usuario")
    password = forms.CharField(
        max_length=100, label="Contraseña", widget=forms.PasswordInput())
    passwordr = forms.CharField(
        max_length=100, label="Repetir contraseña", widget=forms.PasswordInput())

    def clean_password(self):
        cleaned_data = super(TUsuarioCreateForm, self).clean()
        password = cleaned_data.get("password")
        if len(password) < 8:
            raise forms.ValidationError(
                "La contraseña debe tener al menos 8 caracteres"
            )

        if not any(char.isdigit() for char in password):
            raise forms.ValidationError(
                "La contraseña debe contener al menos un numero"
            )

        if not any(char.isupper() for char in password):
            raise forms.ValidationError(
                "La contraseña debe contener al menos una mayuscula"
            )

        if not any(char.islower() for char in password):
            raise forms.ValidationError(
                "La contraseña debe contener al menos una minuscula"
            )

        if not any(char in '!@#$%^&*()_+-=' for char in password):
            raise forms.ValidationError(
                "La contraseña debe contener al menos un caracter especial"
            )

        return password

    def clean_passwordr(self):
        cleaned_data = super(TUsuarioCreateForm, self).clean()
        password = cleaned_data.get("password")
        passwordr = cleaned_data.get("passwordr")

        if password != None:

            if password != passwordr:
                raise forms.ValidationError(
                    "Las contraseñas no coinciden"
                )

        return passwordr

    def clean_nombre(self):
        cleaned_data = super(TUsuarioCreateForm, self).clean()
        nombre = cleaned_data.get("nombre")
        if len(nombre) < 3:
            raise forms.ValidationError(
                "El nombre debe tener al menos 3 caracteres"
            )

        if not nombre.isalpha():
            raise forms.ValidationError(
                "El nombre debe contener solo letras"
            )

        return nombre

    def clean_apellidoP(self):
        cleaned_data = super(TUsuarioCreateForm, self).clean()
        apellidoP = cleaned_data.get("apellidoP")

        if len(apellidoP) < 3:
            raise forms.ValidationError(
                "El apellido paterno debe tener al menos 3 caracteres"
            )

        if not apellidoP.isalpha():
            raise forms.ValidationError(
                "El apellido paterno debe contener solo letras"
            )

        return apellidoP

    def clean_apellidoM(self):
        cleaned_data = super(TUsuarioCreateForm, self).clean()
        apellidoM = cleaned_data.get("apellidoM")

        if len(apellidoM) < 3:
            raise forms.ValidationError(
                "El apellido materno debe tener al menos 3 caracteres"
            )

        if not apellidoM.isalpha():
            raise forms.ValidationError(
                "El apellido materno debe contener solo letras"
            )

        return apellidoM

    def __init__(self, *args, **kwargs):
        super(TUsuarioCreateForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Nombre de usuario'})
        self.fields['correo'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Correo'})
        self.fields['nombre'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Nombre'})
        self.fields['apellidoP'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Apellido paterno'})
        self.fields['apellidoM'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Apellido materno'})

        self.fields['password'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Contraseña', 'data-toggle': 'password'})
        self.fields['passwordr'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Repetir contraseña'})
