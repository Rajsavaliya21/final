from django.urls import path
from .views import *
urlpatterns = [
    path('',selectUser,name='selectuser'),
    path('Ownerlogin/',OwnerLogin,name='login'),
    path('Owner/logout/',logout,name='logout'),
    path('Owner/forgotpassword/',ForgotPassword,name='forgotpassword'),
    path('Owner/verifyotp',VerifyOtp,name='verifyotp'),
    path('Owner/createnewpassword',CreateNewPassword,name='createnewpassword'),
]
