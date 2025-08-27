from django.shortcuts import render,redirect
from myapp.models import categoryDB,productDB
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError

from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login




# Create your views here.
def dashboard(request):
    categories = categoryDB.objects.count()
    product = productDB.objects.count()
    return render(request,"dashboard.html",{'categories':categories,'product':product})
def category(request):
    return render(request,"add_category.html")
def save_category(request):
    if request.method=="POST":
        cate_name=request.POST.get("cname")
        cate_img=request.FILES['image']
        cate_des=request.POST.get("desc")
        obj=categoryDB(catename=cate_name,cimage=cate_img,description=cate_des)
        obj.save()
        return redirect('category')

def disp_cate(request):
    category=categoryDB.objects.all()
    return render(request,"disp_category.html",{'category':category})
def cate_delete(request,ci):
    category=categoryDB.objects.get(id=ci)
    category.delete()
    return redirect('disp_cate')
def cate_edit(request,ci):
    category=categoryDB.objects.get(id=ci)
    return render(request,"edit_category.html",{'category':category})

def category_update(request,cr):
    if request.method=="POST":
        cate_name=request.POST.get("cname")
        cate_des=request.POST.get("desc")
        try:
            cate_img = request.FILES['image']
            fs = FileSystemStorage()
            filename=fs.save(cate_img.name,cate_img)
        except MultiValueDictKeyError:
            filename=categoryDB.objects.get(id=cr).cimage
    categoryDB.objects.filter(id=cr).update(catename=cate_name,description=cate_des,cimage=filename)
    return redirect('disp_cate')



# **********************************************************************************************************
def add_product(request):
    category = categoryDB.objects.all()
    return render(request,"add_product.html",{'category':category})
def save_product(request):
    if request.method=="POST":
        p_selct=request.POST.get("sname")
        p_name=request.POST.get("pname")
        p_img=request.FILES['pimage']
        p_price = request.POST.get("price")
        p_des = request.POST.get("des")
        obj=productDB(select_pro=p_selct,proname=p_name,proimg=p_img,cost=p_price,pdesc=p_des)
        obj.save()
        return redirect('add_product')
def product_disp(request):
    product=productDB.objects.all()
    return render(request,"product_dis.html",{'product':product})
def product_delete(request,pi):
    product=productDB.objects.get(id=pi)
    product.delete()
    return redirect('product_disp')

def pro_edit(request,pi):
    product=productDB.objects.get(id=pi)
    categories=categoryDB.objects.all()
    return render(request,"product_edit.html",{'product':product,'categories':categories})
def update_product(request, pr):
    if request.method == "POST":
        p_selct = request.POST.get("sname")
        p_name = request.POST.get("pname")
        p_price = request.POST.get("price")
        p_des = request.POST.get("des")


        try:
            p_img = request.FILES['pimage']
            fs = FileSystemStorage()
            filename = fs.save(p_img.name,p_img)
        except MultiValueDictKeyError:

            filename =productDB.objects.get(id=pr).proimg

    productDB.objects.filter(id=pr).update(select_pro=p_selct,proname=p_name,proimg=filename,cost=p_price,pdesc=p_des)
    return redirect('product_disp')

def admin_login_page(request):
    return render(request,"login.html")
def admin_login(request):
    if request.method=="POST":
        uname=request.POST.get("username")
        psd=request.POST.get("password")
        if User.objects.filter(username__contains=uname).exists():
            X=authenticate(username=uname,password=psd)
            if X is not None:
                login(request, X)
                request.session['username'] = uname
                request.session['password'] = psd
                return redirect(dashboard)
            else:
                return redirect(admin_login_page)
        else:
            return redirect(admin_login_page)

def admin_logout(request):
    if "username" in request.session:
        del request.session['username']
    if "password" in request.session:
        del request.session['password']
    return redirect('admin_login_page')






