from django.contrib import admin 
from bitrix_report_1c.models import Montajnik_1C
from .models import user_id, Core_Supervizer 
from django.contrib.auth.models import User

@admin.register(user_id)
class AgentAdmin(admin.ModelAdmin):
    
    exclude = ['bx_id']
    list_display = ('bx_id', 'teleid', 'surname', 'supervizer_surname', 'hydra_id_sales', 'region', 'supervizer')


@admin.register(Core_Supervizer)
class SupervizerAdmin(admin.ModelAdmin):
    list_display = ('supervizer_surname','region', 'supervizer_id')

@admin.register(Montajnik_1C)
class Montajnik_1C_Admin(admin.ModelAdmin):
    exclude = ['bx_id']
    list_display = ('id','bx_id','id_mont', 'fio_mont')













