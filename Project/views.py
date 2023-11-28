from django.shortcuts import redirect, render
from django.contrib import messages
# from django.core.mail import send_mail
from authentication.helpers import require_access_token
from authentication.models import TenantAuth
from .models import AddProperty
# Create your views here.
@require_access_token
def dashboard(request):
    return render(request,'dashboard.html')

@require_access_token
def addProperty(request):
    if request.method == 'POST':
        property_name = request.POST.get('propertyName')
        house_no = request.POST.get('houseNo')
        society_name = request.POST.get('societyName')
        landmark = request.POST.get('landmark')
        city = request.POST.get('city')
        state = request.POST.get('state')
        pincode = request.POST.get('pincode')
        owner = request.session.get('user_id')
    

        add = AddProperty.objects.create(
            owner_id = owner ,property_name = property_name,
            house_number = house_no,
            society_name = society_name,
            landmark = landmark,
            city = city,
            state = state,
            pincode = pincode )
        
        add.save()
        messages.success(request,'Added Property Succesfully')

  
        return redirect('addproperty')


    return render(request,'addproperty.html')

@require_access_token


def addTenant(request):
    if request.method == 'POST':
        owner = request.session.get('user_id')
        first_name = request.POST.get('FirstName')
        last_name = request.POST.get('LastName')
        email = request.POST.get('Email')
        mobile_no = request.POST.get('MobileNo')
        password = request.POST.get('Password')

        try:
            CHECK = TenantAuth.objects.get(email=email)
            messages.error(request, 'Tenant Already Registered')
         
        except TenantAuth.DoesNotExist:
            add = TenantAuth(
                    owner_id=owner,
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    mobile_number=mobile_no,
                    password=password
                )
            add.save()
            # subject = 'Registration Confirmed and Login Credentials'
            # message = f'Dear {first_name} {last_name} Your Credential for login are Email - {email} & Password - {password}'
            # from_email = 'testdjangorj@gmail.com'
            # recipient_list = [email]

            # send_mail(subject,message,from_email,recipient_list)
            messages.success(request, 'Tenant Added ')
            return redirect('addtenant')

    return render(request,'addtenant.html')

@require_access_token
def allotproperty(request):
    return render(request,'allotproperty.html')
