from django.shortcuts import render

from app.forms import NewUserForm
from app.models import *



from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    categories = Categories.objects.all()[:4]
    name = request.user
    products = Products.objects.all()[:4]
    cat_list = Categories.objects.all()
    return render(request,"index.html",{'cat':categories,'name':name,'product':products,'cat_list':cat_list})


@login_required
def user_logout(request):
    logout(request)
    categories = Categories.objects.all()
    return HttpResponseRedirect(reverse(index))


def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")


        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect('/')
            else:
                return HttpResponse("Please Active Your Account")
        else:
            msg = "Invalid Credentials..."
            return render(request,"login.html",{"msg":msg})
    else:
        return render(request,"login.html")




def registration(request):
    registered = False

    if request.method == "POST":
        user_form = NewUserForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print(user_form.errors, NewUserForm.errors)

    else:
        user_form = NewUserForm
    return render(request,"registration.html",
                  {
                      'user_form': user_form,
                      'registered': registered,
                  })


def prod_list(request):
    prod_id = request.GET.get("prod_id")
    cat_list = Categories.objects.all()
    data = Products.objects.filter(prod_category=prod_id)
    print(data)
    return render(request,"prod_list.html",{"data":data,'cat_list':cat_list})


def profile(request):
    cat_list = Categories.objects.all()
    return render(request,'profile.html',{'cat_list':cat_list,})


def product(request):
    cat_list = Categories.objects.all()
    prod_id = request.GET.get("prod_id")
    data = Products.objects.filter(prod_id=prod_id)
    return render(request,"product.html",{'cat_list':cat_list,'data':data})