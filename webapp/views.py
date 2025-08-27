from django.shortcuts import render,redirect
from django.template.context_processors import request

from myapp.models import categoryDB,productDB
from webapp.models import userDB,cartDB,checkoutDB
from django.contrib import messages
from webapp.decorators import session_login_required
# Create your views here.
def home(request):
    category=categoryDB.objects.all()
    cart_total = 0
    name = request.session.get('name')
    if name:
        cart_total = cartDB.objects.filter(username=name).count()
    return render(request,"home.html",{'category':category,'cart_total':cart_total})
def blog(request):
    category = categoryDB.objects.all()
    cart_total = 0
    name = request.session.get('name')
    if name:
        cart_total = cartDB.objects.filter(username=name).count()
    products=productDB.objects.all()
    return render(request,"blog.html",{'products':products,'cart_total':cart_total,'category':category})
def single_book(request,book_id):
    product=productDB.objects.get(id=book_id)
    category = categoryDB.objects.all()
    cart_total = 0
    name = request.session.get('name')
    if name:
        cart_total = cartDB.objects.filter(username=name).count()

    return render(request,"single_book.html",{'product':product,'cart_total':cart_total,'category':category})
def filterd_books(request,cate_name):
    products=productDB.objects.filter(select_pro=cate_name) # filter(id=proid)
    return render(request,"filterd_books.html",{'products':products})
def books_page(request):
    category = categoryDB.objects.all()
    cart_total = 0
    name = request.session.get('name')
    if name:
        cart_total = cartDB.objects.filter(username=name).count()
    product=productDB.objects.all()
    return render(request,"book.html",{'product':product,'cart_total':cart_total,'category':category})
def about_page(request):
    category = categoryDB.objects.all()

    cart_total = 0
    name = request.session.get('name')
    if name:
        cart_total = cartDB.objects.filter(username=name).count()
    return render(request,"about.html",{'cart_total':cart_total,'category':category})
def contact_page(request):
    category = categoryDB.objects.all()

    cart_total = 0
    name = request.session.get('name')
    if name:
        cart_total = cartDB.objects.filter(username=name).count()
    return render(request, "contact.html",{'cart_total':cart_total,'category':category})
def user_sign_in(request):
    return render(request,"sign_in.html")
def user_sign_up(request):
    return render(request,"sign_up.html")
def signup(request):
    if request.method=="POST":
        username=request.POST.get("user")
        upsd=request.POST.get("password")
        cpsd=request.POST.get("conform password")
        email=request.POST.get("email")
        obj= userDB (uname=username,u_password=upsd,c_password=cpsd,email_address=email)
        if userDB.objects.filter(uname=username).exists():
            messages.success(request,"User already exists ..!")
            return redirect(user_sign_up)
        elif userDB.objects.filter(email_address=email).exists():
            messages.warning(request,"Email already exits")
            return redirect(user_sign_up)
        else:
            obj.save()
            return redirect()






def login(request):
    if request.method == "POST":
        un = request.POST.get("username")
        pswd = request.POST.get("password")

        try:
            user = userDB.objects.get(uname=un)
            if user.u_password == pswd:
                request.session['name'] = un
                request.session['u_password'] = pswd
                messages.success(request, "Welcome to homepage!")
                return redirect(home)
            else:
                messages.warning(request, "Incorrect password")
                return redirect(user_sign_in)
        except userDB.DoesNotExist:
            messages.warning(request, "Username does not exist")
            return redirect(user_sign_in)
    else:
        return redirect(user_sign_in)




def user_logout(request):
    del request.session['name']
    del request.session['u_password']
    return redirect(home)

def cart_page(request):
    # calculating the total amount
    sub_total=0
    delivery_charge=0
    total_amount=0

    data=cartDB.objects.filter(username=request.session['name'])
    for i in data:
        sub_total +=i.totalprice
        if sub_total>500:
            delivery_charge=50
        else:
            delivery_charge=100
        total_amount=sub_total + delivery_charge
    return render(request,"cart.html",{'data':data,'sub_total':sub_total,'delivery_charge':delivery_charge,'total_amount':total_amount})

@ session_login_required
def save_cart(request):
    if request.method=="POST":
        pro_name = request.POST.get("pname")
        qty = int(request.POST.get("quantity"))
        price = request.POST.get("price")
        total_price = request.POST.get("totalprice")
        u_name = request.POST.get("username")
        existing_cart_items = cartDB.objects.filter(username=u_name, productname=pro_name)
        if existing_cart_items.exists():
            # Merge quantities if duplicats found
            cart_item = existing_cart_items.first()  # pick the first item
            total_quatity = cart_item.quantity + qty
            cart_item.quantity = total_quatity
            cart_item.total_price = cart_item.quantity * cart_item.price
            cart_item.save()
            # Delete other duplicate entries if any
            if existing_cart_items.count() > 1:
                existing_cart_items.exclude(id=cart_item.id).delete()
        else:
            product = productDB.objects.filter(proname=pro_name).first()

            img = product.proimg if product else None

            obj = cartDB(username=u_name, productname=pro_name, quantity=qty, price=price, totalprice=total_price, prod_img=img)
            obj.save()
    return redirect(home)

def Update_cart_quantity(request,item_id):
    if request.method=="POST":
        qty= request.POST.get('action')
        try:
            cart_item=cartDB.objects.get(id=item_id)
            if  qty =="increase":
                cart_item.quantity += 1
            elif qty =="decrease":
                if cart_item.quantity > 1:
                    cart_item.quantity -=1
                else:
                    cart_item.delete() # remove from cart if quantity reaches 0
                    return  redirect(cart_page)
            cart_item.totalprice=cart_item.quantity * cart_item.price
            cart_item.save()
        except cartDB.DoesNotExists:
            pass
    return redirect(cart_page)






def cart_delete(request,cart_id):
    data=cartDB.objects.filter(id=cart_id)
    data.delete()
    return redirect(cart_page)


def checkout_page(request):
        category = categoryDB.objects.all()
        cart_total = 0
        name = request.session.get('name')
        if name:
            cart_total = cartDB.objects.filter(username=name).count()

        sub_total = 0
        delivery_charge = 0
        total_amount = 0

        data = cartDB.objects.filter(username=request.session['name'])
        for i in data:
            sub_total += i.totalprice
            if sub_total > 500:
                delivery_charge = 50
            else:
                delivery_charge = 100
            total_amount = sub_total + delivery_charge
        if request.method == "POST":
            first_name = request.POST.get('nname')
            second_name = request.POST.get('sname')
            ema = request.POST.get('email')
            add = request.POST.get('address')
            state = request.POST.get('state')
            place = request.POST.get('location')
            phone = request.POST.get('mob')
            postcode = request.POST.get('pin')
            total = request.POST.get('total')
            obj = checkoutDB(firstname=first_name, lastname=second_name, Email=ema, Address=add,
                             place=place, state=state, Mobile=phone, pin=postcode, Totalprice=total)
            obj.save()
            return redirect(payment)

        return render(request, "checkout_page.html", {'category': category, 'cart_total': cart_total, 'sub_total': sub_total,
                                                 'delivery_charge': delivery_charge, 'total_amount': total_amount})
def payment(request):
    category = categoryDB.objects.all()
    cart_total = 0
    name = request.session.get('name')
    if name:
        cart_total = cartDB.objects.filter(username=name).count()


    customer = checkoutDB.objects.order_by('-id').first()
    # get the amount of the specified customer
    payy = customer.Totalprice
    amount = int(payy * 100)
    payy_str = int(amount)
    if request.method == "POST":
        order_currency = 'INR'
        client = razorpay.client(auth=('rzp_test_0ib0jPwwZ7I1lT', 'VjHNO5zKeKxz8PYe7VnzwxMR'))
        payment = client.order.create({'amount': amount, 'currency': order_currency})

    return render(request,"payment.html",{'category':category,'cart_total':cart_total,'payy_str':payy_str})