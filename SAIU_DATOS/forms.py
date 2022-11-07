from .models import Noviembre
from django import forms

class estadisticasNoviembre(forms.ModelForm):
    class Meta:
        model = Noviembre
        fields = "__all__"