# forms.py

import logging

from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from localflavor.br.forms import BRCPFField

from .models import ExtraInfo

logger = logging.getLogger(__name__)
class ExtraInfoForm(ModelForm):
    cpf = BRCPFField(label=_("CPF"), required=True)
    def __init__(self, *args, **kwargs):
        super(ExtraInfoForm, self).__init__(*args, **kwargs)
        logger.debug("Initializing ExtraInfoForm with fields: %s", self.fields)
        self.fields['cpf'].required = True

    class Meta:
        model = ExtraInfo
        fields = ('cpf',)
        labels = {'cpf': 'CPF'}
        help_texts = {'cpf': 'Informe seu CPF'}
