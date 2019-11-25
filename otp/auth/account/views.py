from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User , PhoneoTP
from django.shortcuts import get_object_or_404

# Create your views here.
import random
class ValidatePhoneSendOTP(APIView):


    def post(self,request,*args,**kargs):
        phone_number = request.data.get('phone')
        
        if phone_number:
            phone = str(phone_number)
            user = User.object.filter(phone_iexact = phone)
            if user.exists():
                return Response({
                    'status':False,
                    'details':"Phone number is already exist"
                })
            else:
                key=send_otp(phone)
                if key:
                    PhoneoTP.objects.create(
                        phone=phone,
                        otp=key,
                    )

                else:
                    return Response({
                        'status':False,
                        'details':"sending otp error"
                    })


        else:
            return Response({
                'status':False,
                'details':'Phone number is not given in post request'
            })
def send_otp(phone):
    if phone:
        key= random.randint(999,9999)
        return key
    else:
        return False
 