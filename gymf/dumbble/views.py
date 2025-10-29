from django.shortcuts import render, get_object_or_404, redirect
from .models import*
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.


def index(request):
    return render(request, "index.html")


def error_404(request):
    return render(request, "404.html")


def about_us(request):
    return render(request, "about-us.html")


def blog_details(request):
    return render(request, "blog-details.html")


def blog(request):
    return render(request, "blog.html")


def bmi_calculator(request):
    return render(request, "bmi-calculator.html")


def class_details(request):
    return render(request, "class-details.html")


def class_timetable(request):
    return render(request, "class-timetable.html")


def contact(request):
    return render(request, "contact.html")


def gallery(request):
    return render(request, "gallery.html")


def main(request):
    return render(request, "main.html")


def services(request):
    return render(request, "services.html")


def team(request):
    return render(request, "team.html")


def product(request):
    products = Product.objects.all()
    

    # You can also group them by category
    supplements = products.filter(category="Supplement")
    equipments = products.filter(category="Equipment")

    # Send to template
    return render(
        request,
        "product.html",
        {
            "supplements": supplements,
            "equipments": equipments,
        },
    )


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, "product_details.html", {"product": product})


# def checkout_view(request):
#     cart = request.session.get('cart', {})
#     cart_items = []
#     total = 0

#     for product_id, qty in cart.items():
#         product = Product.objects.get(id=product_id)
#         subtotal = product.price * qty
#         cart_items.append({'product': product, 'quantity': qty, 'total': subtotal})
#         total += subtotal

#     return render(request, 'checkout.html', {
#         'cart_items': cart_items,
#         'cart_total': total
#     })


def thankyou(request):
    return render(request, "thankyou.html")


def checkout(request):
    if request.method == "POST":
        # cart_items = CartItem.objects.filter(user=request.user)  # ✅ Fixed filter line

        first_name = request.POST["firstName"]
        last_name = request.POST["lastName"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        address1 = request.POST["address1"]
        address2 = request.POST["address2"]
        city = request.POST["city"]
        state = request.POST["state"]
        zip_code = request.POST["zipCode"]
        country = request.POST["country"]

        Checkout.objects.create(
            user=request.user,
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            address1=address1,
            address2=address2,
            city=city,
            state=state,
            zip_code=zip_code,
            country=country,
        )

        return redirect("thankyou")

    return render(request, "checkout.html")
# def checkout(request):
#     return render(request,'checkout.html')



