from django.contrib import admin
from django.utils.html import format_html
from .models import Category,Item,Customer,ItemOrder,Order,Address,Itemlocation,location



   

class ItemAdmin(admin.ModelAdmin):
    list_display=['Name','Price','Category','Quantity','image_tag']
    list_filter=['Category']
    readonly_fields = ('Author',)
    def image_tag(self,obj):
        return format_html('<img src="{0}" style="width: 45px; height:45px;" />'.format(obj.Image.url))
   
    def save_model(self, request, obj, form, change):
        obj.Author = request.user
        super(ItemAdmin, self).save_model(request, obj, form, change)


class OrderAdmin(admin.ModelAdmin):
    list_display=['products','total_price']
    list_filter=['is_ordered']
    def products(self, obj):
        x=""
        qs=obj.items.all()
        for p in qs:
            if p == qs.last():
                x+=p.item.Name + " X " + str(p.quantity) 
            else:
                x+=p.item.Name + " X " + str(p.quantity) + " - "
        
        return x
    

# Register your models here.
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Item,ItemAdmin)
admin.site.register(ItemOrder)
admin.site.register(Order,OrderAdmin)
admin.site.register(Address)
admin.site.register(Itemlocation)
admin.site.register(location)


    