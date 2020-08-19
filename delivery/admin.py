from django.contrib import admin
from rangefilter.filter import DateRangeFilter
from .views import printforstore
from delivery.models import Order,Store,Driver
@admin.register(Order)
class NewOrderAdmin(admin.ModelAdmin):
    list_display=('adder','orderfee','driver','deliverfee','created_at','status')
    readonly_fields=['store','desc','orderfee','adder','customername','phone']
    list_filter = ['store','status','driver',
        ('created_at', DateRangeFilter),]

    actions = ['print_orders',]


    def has_add_permission(self, request):
        return False


    def print_orders(self,request,queryset):
        return printforstore(request,queryset)


class StoreAdmin(admin.ModelAdmin):
    list_display=('adder','user','name','get_phone')

    def get_phone(self, obj):
        return obj.user.phone

    get_phone.short_description = 'جوال المتجر'

class DriverAdmin(admin.ModelAdmin):
    list_display=('city','get_phone','name')

    def get_phone(self, obj):
        return obj.user.phone

    get_phone.short_description = 'جوال المتجر'



admin.site.register(Store,StoreAdmin)
admin.site.register(Driver,DriverAdmin)


