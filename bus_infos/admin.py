from django.contrib import admin
from .models import CarType,BusInfo,CarChangeLog,RouteInfo

#Register your models here.
class CarChangeLogInline(admin.TabularInline):
    model = CarChangeLog
    extra = 1
def change_to_2(modelAdmin, request, queryset):  #queryset：选中的集合；modelAdmin代表BookAdmin类,相当于self
    print("----->", modelAdmin,request,queryset)
    queryset.update(team="2")
change_to_2.short_description = "设置为2车队"

class BusInfoAdmin(admin.ModelAdmin):
    fieldsets=[
        ('车牌号',{'fields':['car_id']}),
        ('登记日期',{'fields':['published_date'],'classes':['collapse']}),
        ('线路',{'fields':['route']}),
        ('公司',{'fields':['company']}),
        ('车型',{'fields':['cartype']}),
        ('所属车队',{'fields':['team','scrap']})
    ]
    actions = [change_to_2]
    inlines = [CarChangeLogInline]
    list_display = ('car_id', 'route','team')
    list_filter = ["route__team","cartype__power_type"]
    search_fields = ['route']
    save_as = True

class CarTypeAdmin(admin.ModelAdmin):
    fieldsets = [
        ('车型', {'fields': ['type_name']}),
        ('公司简称', {'fields': ['subname']}),
        ('公司全称', {'fields': ['company_name']}),
        ('车长', {'fields': ['car_length']}),
        ('能耗类型', {'fields': ['power_type']}),
        ('载客量', {'fields': ['bus_load']}),
    ]

    list_display = ( 'type_name','subname')

class RouteInfoAdmin(admin.ModelAdmin):
    fieldsets = [
        ('车队', {'fields': ['team']}),
        ('线路名称', {'fields': ['routename']})
    ]

    list_display = ( 'routename','team')


admin.site.register(BusInfo,BusInfoAdmin)
admin.site.register(CarType,CarTypeAdmin)
admin.site.register(RouteInfo,RouteInfoAdmin)