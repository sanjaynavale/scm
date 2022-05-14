import datetime

from django.shortcuts import render

# Create your views here.
from .models import User,Book_ground,Admin


def index(request):
    return render(request,"index.html")
def about(request):
    return render(request,"about.html")
def user_reg(request):
    return render(request,"user_reg.html")

def user_test(request):
    if request.method=='POST':
        name=request.POST.get("uname")
        email=request.POST.get("email")
        gender=request.POST.get("gender")
        password=request.POST.get("password")
        contact=request.POST.get("contact")
        record=User(name=name,email=email,gender=gender,password=password,contact=contact)
        record.save()
        return render(request,"user_login.html")
def user_login(request):
    if 'u_name' in request.session:
        param={'name':request.session.get("u_name")}
        return render(request,"userhome.html",param)
    return render(request, "user_login.html")

def user_check(request):
    if request.method == 'POST':
        uname=request.POST.get("uname")
        password=request.POST.get("password")

        try:
            user=User.objects.get(name=uname)

            if user.password==password:
                request.session['u_name']=uname

                return userhome(request)
            else:
                param = {"msg": "PAssword is not exists.."}
                return render(request, "user_login.html", param)
        except Exception as e:
            param={"msg":"This username is not exists.."}
            return render(request,"user_login.html",param)


def userhome(request):
    if 'u_name' in request.session:
        uname=request.session.get("u_name")
        param={"name":uname}
        return render(request,"userhome.html",param)
    else:
        param={"status":"You need to Login"}
        return render(request,"user_login",param)

def ground_booking(request):
    if 'u_name' in request.session:
        param={'date':datetime.date.today}
        return  render(request,"ground_booking.html",param)
    else:
        param={'status':"You Need to Login ..!!!"}
        return  render(request,"user_reg",param)

def data_ground_booking(request):
    if request.method == 'POST':
        date=request.POST.get("date")
        time=request.POST.get("time")
        try:
            book=Book_ground.objects.get(date=date)
            param={'status':'Please select other date..'}
            return render(request,"ground_booking.html",param)
        except Exception as e:
            user=User.objects.get(name=request.session.get("u_name"))
            book=Book_ground(uid=user.uid,name=user.name,date=date,time=time,mobile=user.contact)
            book.save()
            param={'status':'Booking Succssefull...'}
            return render(request,"userhome.html",param)
    else:
        param={"msg":"Something wrong"}
        return render(request,"ground_booking.html",param)

def admin_login_page(request):
    if 'a_name' in request.session:
        param={'name':request.session.get("a_name")}
        return render(request,"adminhome.html",param)
    return render(request,"admin_login.html")

def admin_check(request):
    if request.method == 'POST':
        aname=request.POST.get("aname")
        password=request.POST.get("password")

        try:
            ad=Admin.objects.get(name=aname)

            if ad.password==password:
                request.session['a_name']=aname

                return adminhome(request)
            else:
                param = {"msg": "PAssword is not exists.."}
                return render(request, "admin_login.html", param)
        except Exception as e:
            param={"msg":"This username is not exists.."}
            return render(request,"admin_login.html",param)

def adminhome(request):
    if 'a_name' in request.session:
        aname = request.session.get("a_name")
        param = {"name": aname}
        return render(request, "adminhome.html", param)
    else:
        param = {"status": "You need to Login"}
        return render(request, "user_login", param)

def admin_booking(request):
    if 'a_name' in request.session:
        booking=Book_ground.objects.all()
        param={'data':booking}
        return render(request,"admin_booking.html",param)
    else:
        param={'status':"Your Need to Login"}
        return render(request,"admin_login.html",param)