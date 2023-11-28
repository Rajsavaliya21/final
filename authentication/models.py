from django.db import models

# Create your models here.

class OwnerAuth(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)
    owner_otp = models.CharField(max_length=6,null=True,blank=True)

    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class TenantAuth(models.Model):
    owner = models.ForeignKey(OwnerAuth,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)
    mobile_number = models.CharField(max_length=10)
    tenant_otp = models.CharField(max_length=6,null=True,blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'