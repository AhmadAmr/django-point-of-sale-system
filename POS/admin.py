from django.contrib import admin
from .models import Category,Item,Customer,ItemOrder,Order,Address



   

class ItemAdmin(admin.ModelAdmin):
    readonly_fields = ('Author',)
    def save_model(self, request, obj, form, change):
        obj.Author = request.user
        super(ItemAdmin, self).save_model(request, obj, form, change)
    
    

# Register your models here.
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Item,ItemAdmin)
admin.site.register(ItemOrder)
admin.site.register(Order)
admin.site.register(Address)


    