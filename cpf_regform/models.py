
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
    
    def clean_cpf(self):
        return self.cpf
    def __str__(self):
        result = '{0.user} {0.cpf}'
        return result.format(self)