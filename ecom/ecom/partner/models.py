from django.db import models
from oscar.apps.partner.abstract_models import AbstractPartner


class Partner(AbstractPartner):
    gst_number = models.CharField(max_length=15, default='00ABCDEF12340Z0', editable=False)

from oscar.apps.partner.models import *  