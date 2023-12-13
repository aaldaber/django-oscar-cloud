from django.db import models
from oscar.apps.order.abstract_models import AbstractOrder


class Order(AbstractOrder):
    qr_code_sync = models.BinaryField(null=True, blank=True, default=None,
                                      verbose_name="Sync QR code pic in binary format")
    qr_code_sync_datetime = models.DateTimeField(null=True, blank=True, default=None,
                                                 verbose_name="Sync QR code date written")

from oscar.apps.order.models import *  # noqa isort:skip
