from django.forms import ModelForm
from localflavor.br.forms import BRCPFField

from .models import ExtraInfo


class ExtraInfoForm(ModelForm):

    cpf = BRCPFField
    """
    The fields on this form are derived from the ExtraInfo model in models.py.
    """
    def __init__(self, *args, **kwargs):
        super(ExtraInfoForm, self).__init__(*args, **kwargs)
        self.fields['cpf'].required=True

    class Meta(object):
       model = ExtraInfo
       fields = ('cpf')
       labels = {
           'cpf': 'CPF',
       }
       help_text={
           'cpf': 'Insira seu CPF',
       }
    
