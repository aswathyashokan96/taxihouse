from django.shortcuts import render
from adminapp.models import *
from publicapp.views import home
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.
def admin_profile(request):
    try:
        if request.session['userid']:
            return render(request,"adminapp/adminprofile.html",{})
    except KeyError:
        return HttpResponse("you are logout")    
def registration(request):
    try:
        if request.session['userid']:
            msg=""
            if request.method=='POST':
                name=request.POST.get('name')
                uname=request.POST.get('username')
                address=request.POST.get('address')
                gender=request.POST.get('gender')
                email=request.POST.get('email')
                ph_no=request.POST.get('phnumber')
                psswd=request.POST.get('password1')
                rpsswd=request.POST.get('password2')
                if psswd==rpsswd:
                    data=tbl_reg.objects.create(name=name,username=uname,address=address,gender=gender,email=email,phone_no=ph_no,password=psswd,status=1)
                    data=tbl_login.objects.create(uname=email,password=psswd,status=1)
                    msg="Registration successfully done!!!"
                else:
                    msg="Passwords didnt match"
            return render(request,"adminapp/registration.html",{'msg':msg})
    except KeyError:
        return HttpResponse("you are logout")
def add_item(request):
    try:
        if request.session['userid']:
            msg=""
            if request.method=='POST':
                item1=request.POST.get('item_name')
                count1=request.POST.get('n')
                date1=request.POST.get('date')
                data=tbl_item.objects.create(item_name=item1,count=count1,date=date1,status=1)
                msg="success"
            return render(request,"adminapp/add_item.html",{'msg':msg})
    except KeyError:
        return HttpResponse("you are logout")
def view_item(request):
    try:
        if request.session['userid']:
            data=tbl_item.objects.filter(status=1)
            return render(request,"adminapp/view_item.html",{'data':data})
    except KeyError:
        return HttpResponse("you are logout")
def edit_item(request,itemid):
    try:
        if request.session['userid']:
            data=tbl_item.objects.get(id=itemid)
            if request.method=='POST':
                na=request.POST.get('name')
                c1=request.POST.get('c')
                d1=request.POST.get('d')
                data.item_name=na
                data.count=c1
                data.date=d1
                data.save()
                return HttpResponseRedirect(reverse('view_item'))
            return render(request,"adminapp/edit_item.html",{'data':data})
    except KeyError:
        return HttpResponse("you are logout")
def delete_item(request,itemid):
    try:
        if request.session['userid']:
            data=tbl_item.objects.get(id=itemid)
            data.status=0
            data.save()
            return HttpResponseRedirect(reverse('view_item'))
    except KeyError:
        return HttpResponse("you are logout")

