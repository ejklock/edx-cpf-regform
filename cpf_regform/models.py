
from django.conf import settings
from django.db import models
from localflavor.br.models import BRCPFField

# Backwards compatible settings.AUTH_USER_MODEL
USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


class ExtraInfo(models.Model):
    """
    This model contains two extra fields that will be saved when a user registers.
    The form that wraps this model is in the forms.py file.
    """
    user = models.OneToOneField(USER_MODEL, null=True,  related_name='user+', on_delete=models.CASCADE)
    cpf = BRCPFField()
    
    def __init__(self, *args, **kwargs):
        if 'cpf' in kwargs:
            kwargs['cpf'] = self.sanitize_cpf(kwargs['cpf'])
        super().__init__(*args, **kwargs)
    
    @staticmethod
    def sanitize_cpf(cpf):
        return ''.join(filter(str.isdigit, cpf.replace('.', '').replace('-', '')))
    
    def __str__(self):
        result = '{0.user} {0.cpf}'
        return result.format(self)
