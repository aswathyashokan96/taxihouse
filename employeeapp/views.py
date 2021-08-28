from django.shortcuts import render
from adminapp.models import *
from django.db.models import aggregates,Sum
from django.http import HttpResponseRedirect,HttpResponse

# Create your views here.
def employee_profile(request):
    try:
        if request.session['userid']:
            uid=request.session['userid']
            data=tbl_reg.objects.get(id=uid)
            return render(request,'employeeapp/employee_profile.html',{'data':data})
    except KeyError:
        return HttpResponse("you are logout")


        
def view_available_items(request):
    try:
        if request.session['userid']:
            data=tbl_item.objects.filter(status=1)
            return render(request,'employeeapp/view_available_items.html',{'data':data})
    except KeyError:
        return HttpResponse("you are logout")
def booking_item(request,itemid):
        try:
                if request.session['userid']:
                        data=tbl_item.objects.get(id=itemid)
                        data1=tbl_booking.objects.filter(item_id=itemid)
                        sum=0
                        for i in data1:
                                sum=sum+i.count
                        c=data.count
                        c=c-sum
                        if request.method=='POST':
                                na=request.POST.get('name')
                                c1=request.POST.get('c1')
                                d1=request.POST.get('d')
                                data1=tbl_booking.objects.create(item_name=na,item_id=itemid,count=c1,booking_date=d1,status=1)
                                return HttpResponse("registration success")
                return render(request,'employeeapp/booking_item.html',{'data':data,'c':c})
        except KeyError:
                return HttpResponse("you are logout")
def delever_item(request,itemid):
        try:
                if request.session['userid']:
#                       data1=tbl_booking.objects.filter(item_id=itemid,status=1)
#                       c=aggregate(sum(data1.count))
                        data=tbl_item.objects.get(id=itemid)
                        if request.method=='POST':
                                na=request.POST.get('name')
                                c1=request.POST.get('c1')
                                d1=request.POST.get('d')
                                data1=tbl_rented.objects.create(item_name=na,item_id=itemid,count=c1,booking_date=d1,status=1)
                                return HttpResponse("registration success")
                        return render(request,'employeeapp/delever_item.html',{'data':data})
        except KeyError:
                return HttpResponse("you are logout")
