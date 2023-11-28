from django.shortcuts import render,redirect
from django.core.mail import send_mail
from .models import OwnerAuth,TenantAuth
from .helpers import generate_jwt_token,require_access_token,generate_otp,generate_jwt_token_for_password
# Create your views here.
def selectUser(request):
    return render(request,'selectuser.html')
def OwnerLogin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            USER_AUTH = OwnerAuth.objects.get(email=email)
            if USER_AUTH.password == password:
                request.session['access_token']=generate_jwt_token(USER_AUTH.id,USER_AUTH.email)
                request.session['user_id'] = USER_AUTH.id
                return redirect('dashboard')
        except OwnerAuth.DoesNotExist:
            return redirect('login')
    return render(request,'login.html')

@require_access_token
def logout(request):
    request.session.clear()
    return render(request,'login.html')

def ForgotPassword(request):

    if request.method == 'POST':
        email = request.POST.get('email')

        try:
            CHECK_MEMBER = OwnerAuth.objects.get(email=email)
            if CHECK_MEMBER:

                otp_ = generate_otp(6)
                CHECK_MEMBER.owner_otp = otp_
                CHECK_MEMBER.save()

                subject = 'Otp For Reseting Password'
                message = f'Otp for Resting Password of account - {email} is {otp_}'
                from_email = 'testdjangorj@gmail.com'
                recipient_list = [email]

                send_mail(subject,message,from_email,recipient_list)

                return redirect('verifyotp')
        except OwnerAuth.DoesNotExist:
            return redirect('forgotpassword')
    return render(request,'forgotpassword.html')


def VerifyOtp(request):
    if request.method == 'POST':
        otp = request.POST.get('otp')
        try:
            verifyotp = OwnerAuth.objects.get(owner_otp=otp)
            if verifyotp:
                return redirect('createnewpassword')
        except:
            return redirect('verifyotp')
    return render(request,'otpverification.html')


def CreateNewPassword(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        if new_password == confirm_password:
           try:
                user = OwnerAuth.objects.get(email=email)
                user.password = confirm_password
                user.save()
                
                return redirect('login')
           except OwnerAuth.DoesNotExist:
               return redirect('createnewpassword')
        else:
            return redirect('createnewpassword')
    return render(request,'createnewpassword.html')