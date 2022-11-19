"""Admin panel configuration."""

from django.contrib import admin

from .models import Discount, Item, Order, Tax


class ItemAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description", "price", "currency",)
    list_display_links = ("id", "name",)
    search_fields = ("id", "name",)
    list_filter = ("price",)
    save_on_top = True


admin.site.register(Item, ItemAdmin)
admin.site.register(Order)
admin.site.register(Discount)
admin.site.register(Tax)
