from django.forms import ModelForm
from localflavor.br.forms import BRCPFField

from .models import ExtraInfo


class ExtraInfoForm(ModelForm):
    cpf = BRCPFField(label='CPF', help_text='Insira seu CPF',required=True)

    """
    The fields on this form are derived from the ExtraInfo model in models.py.
    """
    def __init__(self, *args, **kwargs):
        super(ExtraInfoForm, self).__init__(*args, **kwargs)
        self.fields['cpf'].required = True

    class Meta:
        model = ExtraInfo
        fields = ('cpf',)  # Ensure this is a tuple, even for a single field
        labels = {
            'cpf': 'CPF',
        }
        help_texts = {
            'cpf': 'Insira seu CPF',
        }
