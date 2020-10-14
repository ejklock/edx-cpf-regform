from .models import ExtraInfo
from django.forms import ModelForm
from localflavor.br.forms import BRCPFField



class ExtraInfoForm(ModelForm):

    cpf = BRCPFField
    """
    The fields on this form are derived from the ExtraInfo model in models.py.
    """
    def __init__(self, *args, **kwargs):
        super(ExtraInfoForm, self).__init__(*args, **kwargs)

    class Meta(object):
       model = ExtraInfo
    
