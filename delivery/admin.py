from django.contrib import admin

# Register your models here.
from delivery.models import Order,Store

class NewOrderAdmin(admin.ModelAdmin):
    list_display=('adder','orderfee','driver','deliverfee')
    readonly_fields=['store','desc','orderfee','adder','customername','phone']



    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

class StoreAdmin(admin.ModelAdmin):
    list_display=('adder','logo','user')

admin.site.register(Order,NewOrderAdmin)
admin.site.register(Store,StoreAdmin)

