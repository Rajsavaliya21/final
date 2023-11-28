import random
import string
from django.http import JsonResponse
from django.shortcuts import redirect
from functools import wraps
import jwt
import datetime

from authentication.models import OwnerAuth

SECRET_KEY = 'yX2a7BcR9eY1z'

def generate_jwt_token(user_id, email):
    """
    Generate a JWT token with user-specific data.
    """
    payload = {
        'user_id': user_id,
        'email': email,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=150)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token


def require_access_token(view_func):
    def _wrapped_view(request, *args, **kwargs):
        token = request.session.get('access_token')
        if token:
            try:
                payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
               
                return view_func(request, *args, **kwargs)
            except jwt.ExpiredSignatureError:
              
                return JsonResponse({'error': 'Token has expired'}, status=401)
            except jwt.DecodeError:
              
                return JsonResponse({'error': 'Invalid token'}, status=401)
        else:
            return JsonResponse({'error': 'Token required'}, status=401)
    return _wrapped_view

def generate_otp(digit):
    otp = ''
    digits = string.digits
    for d in range(digit):
        otp += str(random.randint(1, len(digits)-1))
    return otp

from django.shortcuts import redirect

def verify_otp_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if request.method == 'POST':
            otp = request.POST.get('otp')
            try:
                verifyotp = OwnerAuth.objects.get(owner_otp=otp)
                if verifyotp:
                    return view_func(request, *args, **kwargs)
            except OwnerAuth.DoesNotExist:
                return redirect('verifyotp')  # Redirect to OTP verification page

        return redirect('verifyotp')  # Redirect to OTP verification page for non-POST requests

    return _wrapped_view

def generate_jwt_token_for_password(user_id, email):
    """
    Generate a JWT token with user-specific data.
    """
    payload = {
        'user_id': user_id,
        'email': email,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=3)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token