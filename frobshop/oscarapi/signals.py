from django.dispatch import Signal, receiver
import requests
from django.utils import timezone
from django.conf import settings

oscarapi_post_checkout = Signal(providing_args=["order", "user", "request", "response"])


@receiver(oscarapi_post_checkout)
def qr_callback(sender, **kwargs):
    print("New order posted!")
    order = kwargs.get("order")
    the_qr_code = requests.get("{}/qrcode?data={}".format(settings.QR_CODE_ADDRESS, order.number))
    print("Request status: {}".format(the_qr_code.status_code))
    order.qr_code_sync = the_qr_code.content
    order.qr_code_sync_datetime = timezone.now()
    order.save()
