from django.contrib import admin
from .models import TenantAuth,OwnerAuth
# Register your models here.
admin.site.register(TenantAuth)
admin.site.register(OwnerAuth)
