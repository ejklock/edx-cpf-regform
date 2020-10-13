from .models import ExtraInfo
from django.forms import ModelForm

class ExtraInfoForm(ModelForm):
    """
    The fields on this form are derived from the ExtraInfo model in models.py.
    """
    def __init__(self, *args, **kwargs):
        super(ExtraInfoForm, self).__init__(*args, **kwargs)
        self.fields['cpf'].error_messages = {
            "required": u"O campo CPF é obrigatório.",
            "invalid": u"Inválido",
        }

    class Meta(object):
        model = ExtraInfo
        fields = ('cpf')
