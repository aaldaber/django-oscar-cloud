from django.contrib import admin
from oscar.apps.order.admin import *  # noqa
from oscar.apps.order.admin import OrderAdmin as OscarOrderAdmin
from theshop.order.models import Order


class OrderAdmin(OscarOrderAdmin):
    readonly_fields = ('number', 'total_incl_tax', 'total_excl_tax',
                       'shipping_incl_tax', 'shipping_excl_tax', 'qr_image_tag')


admin.site.unregister(Order)
admin.site.register(Order, OrderAdmin)


