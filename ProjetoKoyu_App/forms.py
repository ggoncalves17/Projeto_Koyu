from django.forms import ModelForm, TextInput
from .models import Utilizador

class UtilizadorForm(ModelForm):
    class Meta:
        model = Utilizador
        fields = ["ut_mail", "ut_pass"]

        # Referência -> https://docs.djangoproject.com/en/5.1/topics/forms/modelforms/
        labels = {
            "ut_mail": "Email",
            "ut_pass": "Password",
        }
        widgets = {
            "ut_mail": TextInput(attrs={"placeholder": "Email"}),
            "ut_pass": TextInput(attrs={"placeholder": "Password", "type": "password"}),
        }
