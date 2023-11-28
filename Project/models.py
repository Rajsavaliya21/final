from django.db import models
from authentication.models import OwnerAuth
# Create your models here.

class AddProperty(models.Model):
    owner = models.ForeignKey(OwnerAuth,on_delete=models.CASCADE)
    property_name = models.CharField(max_length=250)
    house_number = models.CharField(max_length=50)
    society_name = models.CharField(max_length=250)
    landmark = models.CharField(max_length=50,null=True,blank=True)
    city = models.CharField(max_length=150)
    state = models.CharField(max_length=150)
    pincode = models.CharField(max_length=6)

    def __str__(self):
        return f'{self.owner.first_name} {self.owner.last_name} - {self.property_name} - {self.house_number}, {self.society_name}'