from django.shortcuts import render,get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, logout
from django.utils import timezone
from .models import *
from .forms import *
from django.core.mail import send_mail

def home(request):
    return render(request, 'gym/index.html')

def about(request):
    return render(request, 'gym/about.html')

def pricing(request):
    return render(request, 'gym/pricing.html')

def submit(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        plan = request.POST['plan']
        current_date = timezone.now().date()
        data = Membership(name = name,email = email,phone = phone,plan = plan,date_created = current_date)
        data.save()
        print(data)
        if data:    

            messages.success(request, 'Your membership was successfully created!')
            return redirect('home')  # Redirect after successful form submission
        else:
            messages.error(request, 'There was an error with your submission. Please try again.')

    else:
        form = MembershipForm()

    return render(request, 'gym/includes/sections/memberships.html', {'form': form})

def gallery(request):
    return render(request, 'gym/gallery.html')

from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password1']
        confirm_password = request.POST['password2']

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('signup')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect('signup')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return redirect('signup')

        user = User.objects.create_user(username=username, email=email, password=password)
        if user:
            subject = "Welcome to New User😉 – Thank You for Signing Up!"
            message = "Hey Welcome to my website." \
            "Dear User," \
            "Welcome to Profit GYM! We’re thrilled to have you as a part of our community."
            try:
                send_mail(subject, message, settings.EMAIL_HOST_USER, [email])
                login(request, user)  # Log the user in after signup
                messages.success(request, "Account created successfully!")
                return redirect('login')  # replace with your desired success route
            except Exception as e:
                messages.error(request, "Email Server Down !")
                
        else:
            messages.success(request, "Account created successfully!")
            return render(request, 'gym/signup.html')


    return render(request, 'gym/signup.html')

@login_required
def dashboard_view(request):
    return render(request, 'dashboard.html')

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # replace with your actual dashboard url name
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'gym/login.html')


def admin_login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_staff:  # Optional: restrict to staff users
            login(request, user)
            return redirect('admin-dashboard')  # redirect to your admin dashboard page
        else:
            messages.error(request, "Invalid credentials or not authorized as admin.")
            return redirect('admin-login')
    return render(request, 'gym/admin_login.html')

def admin_dashboard(request):
    total_members = Membership.objects.count()

    # Let's say "active members" are those who joined in the last 30 days (example logic)
    from datetime import timedelta
    today = timezone.now().date()
    last_30_days = today - timedelta(days=30)
    
    # If `date_created` is stored as string, convert it to date (recommended to store as DateTimeField)
    # For now, filtering active members is skipped due to data type.
    active_members = total_members  # placeholder logic

    # Placeholder values for demo
    avg_visits = 3.2
    revenue = Membership.objects.all()

    # if revenue.plan == "":
    members = Membership.objects.all()

# Define prices
    prices = {
        "basic": 999,
        "standard": 1999,
        "premium": 3599
    }

    # Initialize total
    total_amount = 0

    # Calculate total
    for member in members:
        membership_type = member.plan.lower()  # assuming the type is a string
        total_amount += prices.get(membership_type, 0)  # default to 0 if type is unexpected

    print("Total Amount:", total_amount)

    context = {
        'total_members': total_members,
        'active_members': active_members,
        'avg_visits': avg_visits,
        'revenue': total_amount,
    }
    return render(request, "gym/admin_dashboard.html", context)

def members(request):
    members = Membership.objects.all().order_by('-id')  # or use '-date_created' if 
    return render(request,"gym/members.html",{'members': members})

def membership_view(request, pk):
    member = get_object_or_404(Membership, pk=pk)
    return render(request, 'gym/membership_view.html', {'member': member})


def membership_update(request, pk):
    member = get_object_or_404(Membership, pk=pk)
    if request.method == 'POST':
        member.name = request.POST.get('name')
        member.email = request.POST.get('email')
        member.phone = request.POST.get('phone')
        member.plan = request.POST.get('plan')
        member.save()
        return redirect('members')
    return render(request, 'gym/membership_update.html', {'member': member})


def membership_delete(request, pk):
    member = get_object_or_404(Membership, pk=pk)
    member.delete()
    return redirect('members')


def logout_view(request):
    logout(request)
    return redirect('login')

def ask_question(request):
    return render(request,"ask.html")


import google.generativeai as genai
from django.conf import settings
from django.shortcuts import render
from .forms import AIBotForm




import google.generativeai as genai
genai.configure(api_key="AIzaSyCxqGt4RKf5VYO6UfnyPJsXlVT1AxQLums")

def get_gemini_response(question):
    try:
        model = genai.GenerativeModel("gemini-2.0-flash")
        response = model.generate_content(question)
        return response.text
    except Exception as e:
        print("Gemini API Error:", e)
        return "Sorry, I couldn't get a response from Gemini right now."

import markdown  # Add this import
from django.contrib.auth.decorators import login_required
@login_required
def ask_gemini(request):
    answer_html = None
    if request.method == 'POST':
        form = AIBotForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            question = form.cleaned_data['question']
            answer = get_gemini_response(question)
            answer_html = markdown.markdown(answer)  # Convert Markdown to HTML
            print(answer)
            AI_bot.objects.create(username=username, question=question, answer=answer)
            return render(request, 'gym/ask.html', {
                'form': AIBotForm(),
                'answer': answer_html
            })
    else:
        form = AIBotForm()

    return render(request, 'gym/ask.html', {'form': form, 'answer': answer_html})