from django.contrib import admin
from adminapp.models import *
# Register your models here.
#username:taxihouse,password:regi123
admin.site.register(tbl_reg)
admin.site.register(tbl_login)
admin.site.register(tbl_item)
admin.site.register(tbl_booking)
admin.site.register(tbl_rented)