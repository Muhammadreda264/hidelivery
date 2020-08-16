from django.contrib import admin

# Register your models here.
from delivery.models import Order,Store,Driver

class NewOrderAdmin(admin.ModelAdmin):
    list_display=('adder','orderfee','driver','deliverfee')
    readonly_fields=['store','desc','orderfee','adder','customername','phone']
    list_filter = ['store','status','driver']



    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

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



admin.site.register(Order,NewOrderAdmin)
admin.site.register(Store,StoreAdmin)
admin.site.register(Driver,DriverAdmin)


