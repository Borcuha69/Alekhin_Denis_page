from django.contrib import admin
from .models import *


class ProductInOrderInline(admin.TabularInline):
    model = ProductInOrder
    extra = 0


class StatusAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active', 'created', 'updated']

    class Meta:
        model = Status


admin.site.register(Status, StatusAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display = ['status', 'customer_name', 'customer_phone', 'total_price', 'created', 'updated']
    search_fields = ['status', 'customer_name']
    inlines = [ProductInOrderInline]

    class Meta:
        model = Order


admin.site.register(Order, OrderAdmin)


class ProductInOrderAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'nmb', 'price_per_item', 'total_price', 'is_active', 'created', 'updated']
    search_fields = ['product', 'order']

    class Meta:
        model = ProductInOrder


admin.site.register(ProductInOrder, ProductInOrderAdmin)


class ProductInBasketAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'nmb', 'price_per_item', 'total_price', 'is_active', 'created', 'updated']

    class Meta:
        model = ProductInBasket

admin.site.register(ProductInBasket, ProductInBasketAdmin)