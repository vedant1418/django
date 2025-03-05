from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout

# Create your views here.
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from .models import Product,Cart,Orders,Address,Payment


def index(req):
    allproducts=Product.objects.all()
    context={"allproducts":allproducts}
    return render(req, "index.html",context)


def validate_password(password):
    # Check minimum length
    if len(password) < 8:
        raise ValidationError("Password must be at least 8 characters long.")

    # Check maximum length
    if len(password) > 128:
        raise ValidationError("Password cannot exceed 128 characters.")

    # Initialize flags for character checks
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    special_characters = "@$!%*?&"

    # Check for character variety
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in special_characters:
            has_special = True

    if not has_upper:
        raise ValidationError("Password must contain at least one uppercase letter.")
    if not has_lower:
        raise ValidationError("Password must contain at least one lowercase letter.")
    if not has_digit:
        raise ValidationError("Password must contain at least one digit.")
    if not has_special:
        raise ValidationError(
            "Password must contain at least one special character (e.g., @$!%*?&)."
        )

    # Check against common passwords
    common_passwords = [
        "password",
        "123456",
        "qwerty",
        "abc123",
    ]  # Add more common passwords
    if password in common_passwords:
        raise ValidationError("This password is too common. Please choose another one.")


def signup(req):
    print(req.method)
    context = {}
    if req.method == "GET":
        return render(req, "signup.html")
    else:
        print(req.method)
        uname = req.POST["uname"]
        upass = req.POST["upass"]
        ucpass = req.POST["ucpass"]
        print(uname, upass, ucpass)

        try:
            validate_password(upass)
        except ValidationError as e:
            context["errmsg"] = str(e)
            return render(req, "signup.html", context)

        if uname == "" or upass == "" or ucpass == "":
            context["errmsg"] = "Field can't be empty"
            return render(req, "signup.html", context)
        elif upass != ucpass:
            context["errmsg"] = "Password and confirm password doesn't match"
            return render(req, "signup.html", context)
        elif uname.isdigit():
            context["errmsg"] = "Username can't be only number"
            return render(req, "signup.html", context)
        elif upass == uname:
            context["errmsg"] = "Password cannot same as username"
            return render(req, "signup.html", context)
        else:
            try:
                userdata = User.objects.create(username=uname, password=upass)
                userdata.set_password(upass)
                userdata.save()
                print(User.objects.all())
                return redirect("signin")
            except:
                print("User already exists")
                context["errmsg"] = "User already exists"
                return render(req, "signup.html", context)


def signin(req):
    if req.method == "POST":
        uname = req.POST["uname"]
        upass = req.POST["upass"]
        context = {}
        if uname == "" or upass == "":
            context["errmsg"] = "Field can't be empty"
            return render(req, "signin.html", context)
        else:
            userdata = authenticate(username=uname, password=upass)
            # print(req.user.password)
            if userdata is not None:
                login(req, userdata)
                return redirect("/")
            else:
                context["errmsg"] = "Invalid username and password"
                return render(req, "signin.html", context)
    else:
        return render(req, "signin.html")


def userlogout(req):
    logout(req)
    return redirect("/")


def request_password_reset(req):
    if req.method == "GET":
        return render(req, "request_password_reset.html")
    else:
        uname = req.POST.get("uname")
        context = {}
        try:
            userdata = User.objects.get(username=uname)
            return redirect("reset_password", uname=userdata.username)

        except User.DoesNotExist:
            context["errmsg"] = "No account found with this username"
            return render(req, "request_password_reset.html", context)


def reset_password(req, uname):
    userdata = User.objects.get(username=uname)
    if req.method == "GET":
        return render(req, "reset_password.html", {"user": userdata.username})
    else:
        upass = req.POST["upass"]
        ucpass = req.POST["ucpass"]
        context = {}
        userdata = User.objects.get(username=uname)
        try:
            if upass == "" or ucpass == "":
                context["errmsg"] = "Field can't be empty"
                return render(req, "reset_password.html", context)
            elif upass != ucpass:
                context["errmsg"] = "Password and confirm password need to match"
                return render(req, "reset_password.html", context)
            else:
                validate_password(upass)
                userdata.set_password(upass)
                userdata.save()
                return redirect("signin")

        except ValidationError as e:
            context["errmsg"] = str(e)
            return render(req, "reset_password.html", context)

def about(req):
    return render(req,"about.html")

def contact(req):
    return render(req,"contact.html")

def mobilelist(req):
    if req.method=="GET":
        allproducts=Product.productmanager.mobile_list()
        print(allproducts)
        context={'allproducts':allproducts}
        return render(req,"index.html",context)
    else:
        allproducts=Product.objects.all()
        print(allproducts)
        context={'allproducts':allproducts}
        return render(req,"index.html",context)
def electronicslist(req):
    if req.method=="GET":
        allproducts=Product.productmanager.electronics_list()
        print(allproducts)
        context={'allproducts':allproducts}
        return render(req,"index.html",context)
    else:
        allproducts=Product.objects.all()
        print(allproducts)
        context={'allproducts':allproducts}
        return render(req,"index.html",context)
def clothlist(req):
    if req.method=="GET":
        allproducts=Product.productmanager.cloth_list()
        print(allproducts)
        context={'allproducts':allproducts}
        return render(req,"index.html",context)
    else:
        allproducts=Product.objects.all()
        print(allproducts)
        context={'allproducts':allproducts}
        return render(req,"index.html",context)
def shoeslist(req):
    if req.method=="GET":
        allproducts=Product.productmanager.shoes_list()
        print(allproducts)
        context={'allproducts':allproducts}
        return render(req,"index.html",context)
    else:
        allproducts=Product.objects.all()
        print(allproducts)
        context={'allproducts':allproducts}
        return render(req,"index.html",context)

def showpricerange(req):
    if req.method=="GET":
        return render(req,"index.html")
    else:
        r1=req.POST["min"]
        r2=req.POST["max"]
        if r1 is not None and r2 is not None and r1.isdigit() and r2.isdigit():
            allproducts=Product.objects.all()
            # allproducts=Product.productmanager.pricerange(r1,r2)
            context={'allproducts':allproducts}
            return render(req,'index.html',context)
        else:
            allproducts=Product.objects.all()
            context={'allproducts':allproducts}
            return render(req,"index.html",context)

def sortingbyprice(req):
    sortoption=req.GET.get("sort")
    if sortoption=="low_to_high":
        allproducts=Product.objects.order_by("price")
        print(allproducts)
    elif sortoption=="high_to_low":
        allproducts=Product.objects.order_by("-price")
        print(allproducts)
    else:
        allproducts=Product.objects.all()
    
    context={'allproducts':allproducts}
    return render(req,"index.html",context)


from django.db.models import Q
from django.contrib import messages
def searchproduct(req):
    query=req.GET["q"]
    if query:
        allproducts=Product.objects.filter(Q(productname__icontains=query)
        |Q(category__icontains=query)
        |Q(description__icontains=query))

        if len(allproducts)==0:
            messages.error(req,"NO result found")
    else:
        allproducts=Product.objects.all()

    context={'allproducts':allproducts}
    return render(req,"index.html",context)

def showcarts(req):
        username=req.user
        allcarts=Cart.objects.filter(userid=username.id)
        print(allcarts,len(allcarts))
        totalitems=len(allcarts)
        totalamount=0
        for x in allcarts:
            totalamount+=x.productid.price*x.qty
        if username.is_authenticated:

            allcarts=Cart.objects.all()
            context={'allcarts':allcarts,"username":username,'totalitems':totalitems,'totalamount':totalamount}
        else:
            allcarts=Cart.objects.all()
            context={'allcarts':allcarts,'totalitems':totalitems,'totalamount':totalamount}

        return render(req,'showcarts.html',context)
def addtocart(req,productid):
        if req.user.is_authenticated:
            userid=req.user
        else:
            userid=None
           
        allproducts=get_object_or_404(Product,productid=productid)
        cartitem,created=Cart.objects.get_or_create(userid=userid,productid=allproducts)
        print(cartitem)
        print(created)

        if not created:
            cartitem.qty+=1
        else:
            cartitem.qty=1
        cartitem.save()
        return redirect("/showcarts")
def removecart(req,productid):
    if req.user.is_authenticated:
        userid=req.user
    else:
        userid=None
    cartitems=Cart.objects.get(productid=productid,userid=userid)
    cartitems.delete()
    return redirect("/showcarts")


from django.shortcuts import redirect
from .models import Cart  # Ensure you are importing the Cart model

def updateqty(req, qv, productid):
    
    if req.user.is_authenticated:
        userid = req.user.id
    else:
        userid = None

    
    cart_item = Cart.objects.filter(productid=productid, userid=userid).first()

    if cart_item is None:
       
        return redirect("/showcarts")

   
    if qv == 1:
       
        cart_item.qty += 1
        cart_item.save()  
    else:
        if cart_item.qty > 1:
           
            cart_item.qty -= 1
            cart_item.save() 
        else:
            
            cart_item.delete()

    return redirect("/showcarts")
from .forms import AddressForm
def addaddress(req):
    if req.user.is_authenticated:
        if req.method=="POST":
            form=AddressForm(req.POST)

            if form.is_valid():
                address=form.save(commit=False)
                address.userid=req.user
                address.save()
                return redirect ('/showaddress')
        else:
            form=AddressForm()

        context={'form':form}
        return render(req,'addaddress.html',context)
    else:
        return redirect('/signin')

def showaddress(req):
    if req.user.is_authenticated:
        address=Address.objects.filter(userid=req.user)
        if req.method=="POST":
            return redirect ("/showcarts")
        context={"address":address}
        return render(req,"showaddress.html",context)
    else:
        return redirect ('/signin')
import razorpay
import random
from django.conf import settings
from django.core.mail import send_mail
def payment(req):
    if req.user.is_authenticated:
        try:
            cartitems=Cart.objects.filter(userid=req.user.id)
            totalamount=sum(i.productid.price*i.qty for i in cartitems)
            print(totalamount)
            userid=req.user

            client = razorpay.Client(auth=("rzp_test_wH0ggQnd7iT3nB", "eZseshY3oSsz2fcHZkTiSlCm"))
            data = { "amount": totalamount*100, "currency": "INR", "receipt": "order_rcptid_11" }
            payment = client.order.create(data=data) # Amount is in currency subunits. Default currency is INR. Hence, 50000 refers to 50000 paise
            
            for items in cartitems:
                orderid=random.randrange(1000,9000000)
                orderdata=Orders.objects.create(orderid=orderid,productid=items.productid,userid=userid,qty=items.qty)
                orderdata.save()

                receiptid=random.randrange(10000000,80000000)
                paymentdata=Payment.objects.create(receiptid=receiptid,orderid=orderdata,userid=userid,totalprice=totalamount)
                paymentdata.save()
            print(orderid,receiptid)
            cartitems.delete()
            subject=f"FlipcartClone Payment Status for your order={orderid}"
            msg=f"Hi {userid},Thank you using my services\n Total Amount Paid by you is {totalamount}"
            emailfrom=settings.EMAIL_HOST_USER
            receiver=[userid]
            send_mail(subject,msg,emailfrom,receiver)
            
            context={"data":payment,"amount":totalamount}

        except:
            context={}    
            context["error"]="An error occured while creating payment. Please try again!"
    
    return render(req,'payment.html',context)




