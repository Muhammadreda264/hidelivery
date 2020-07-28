from django.contrib import admin

# Register your models here.
from delivery.models import Order

class NewOrderAdmin(admin.ModelAdmin):
    list_display=('adder','orderfee','driver','deliverfee')
    readonly_fields=['store','desc','orderfee','adder','customername','phone']



    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False



admin.site.register(Order,NewOrderAdmin)