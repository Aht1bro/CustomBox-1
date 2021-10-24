from django.contrib import admin

from .models import *

class SlideAdmin(admin.ModelAdmin):
    list_display=('id',"image","title",'sub_title')



admin.site.register(Category)
admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Product)
admin.site.register(Slide, SlideAdmin)