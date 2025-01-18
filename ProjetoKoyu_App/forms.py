from django.forms import ModelForm, TextInput
from .models import Utilizador

class UtilizadorForm(ModelForm):
    class Meta:
        model = Utilizador
        fields = ["ut_mail", "password"]

        # Referência -> https://docs.djangoproject.com/en/5.1/topics/forms/modelforms/
        labels = {
            "ut_mail": "Email",
            "password": "Password",
        }
        widgets = {
            "ut_mail": TextInput(attrs={"placeholder": "Email"}),
            "password": TextInput(attrs={"placeholder": "Password", "type": "password"}),
        }