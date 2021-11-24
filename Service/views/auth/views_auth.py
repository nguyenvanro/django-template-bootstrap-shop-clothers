from django.shortcuts import render
from Service.models import LoginQRcode

def LoginPage(request):
    name = 'Welcom to website'
    obj = LoginQRcode.objects.get(id=1)
    context = {
        'name':name,
        'obj':obj
    }
    return render(request, 'auth/login.html',context )