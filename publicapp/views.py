from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect
from adminapp.models import *
# Create your views here.
def home(request):
    msg=""
    if request.method=='POST':
        try:
            uname=request.POST.get('uname')
            psswd=request.POST.get('psswd')
            if tbl_login.objects.filter(uname=uname,password=psswd):
                data=tbl_reg.objects.get(username=uname,password=psswd)
                request.session['userid']=data.id
                if data.status=='admin':
                    return HttpResponseRedirect(reverse('admin_profile'))
                elif data.status=='1':
                    return HttpResponseRedirect(reverse('employee_profile'))
                else:
                    msg="incorrect usernane and password"
            else:
                msg="incorrect usernane and password"
        except Member.DoesNotExist:
            return HttpResponse("ERROR")
    return render(request,"publicapp/home.html",{})
def logout(request):
    try:
        del request.session['userid']
    except KeyError:
        pass
    return HttpResponse("you ara logout")


