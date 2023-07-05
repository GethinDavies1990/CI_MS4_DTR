# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.contrib import admin

# Internal:
from .models import Order, OrderLineItem

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class OrderLineItemAdminInline(admin.TabularInline):
    """
    Admin class for the OrderLineItem model
    """

    model = OrderLineItem
    readonly_fields = ("lineitem_total",)

    fields = (
        "product",
        "quantity",
        "lineitem_total",
    )

    extra = 0


class OrderAdmin(admin.ModelAdmin):
    """
    Admin class for the Order model
    """

    inlines = (OrderLineItemAdminInline,)

    readonly_fields = (
        "order_number",
        "date",
        "delivery_cost",
        "order_total",
        "grand_total",
        "original_bag",
        "stripe_pid",
    )

    fields = (
        "order_number",
        "user_profile",
        "date",
        "full_name",
        "email",
        "phone_number",
        "country",
        "postcode",
        "town_or_city",
        "street_address1",
        "street_address2",
        "county",
        "delivery_cost",
        "order_total",
        "grand_total",
    )

    list_display = (
        "order_number",
        "date",
        "full_name",
        "order_total",
        "delivery_cost",
        "grand_total",
        "original_bag",
        "stripe_pid",
    )

    ordering = ("-date",)


admin.site.register(Order, OrderAdmin)
