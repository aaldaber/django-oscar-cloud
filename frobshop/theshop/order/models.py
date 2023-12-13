from django.db import models
from django.utils.safestring import mark_safe
from oscar.apps.order.abstract_models import AbstractOrder


class Order(AbstractOrder):
    qr_code_sync = models.BinaryField(null=True, blank=True, default=None,
                                      verbose_name="Sync QR code pic in binary format")
    qr_code_sync_datetime = models.DateTimeField(null=True, blank=True, default=None,
                                                 verbose_name="Sync QR code date written")

    def qr_image_tag(self):
        from base64 import b64encode
        return mark_safe('<img src="data:image/png;base64,{}">'.format(
            b64encode(self.qr_code_sync).decode('utf8')
        ))

    qr_image_tag.short_description = 'Image'
    qr_image_tag.allow_tags = True

from oscar.apps.order.models import *  # noqa isort:skip
