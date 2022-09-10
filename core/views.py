from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Profile, Donation
from .forms import CustomUserCreationForm, ProfileForm
from django.contrib.auth.models import User
# Create your views here.
def home(request):
    return render(request,'index.html')


def profiles(request):
    return render(request, 'profiles.html')

def gallery(request):
    return render(request, 'gallery.html')

def blog(request):
    return render(request, 'blog.html')

def blogTrial(request):
    return render(request, 'blog_trial.html')

def loginPage(request):
    return render(request, 'login_register.html')

@login_required(login_url='login')
def donatePage(request):
    
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('name')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zipcode = request.POST.get('zipcode')
        card_name = request.POST.get('card_name')
        card_number = request.POST.get('card_number')
        exp_month = request.POST.get('exp_month')
        exp_year = request.POST.get('exp_year')
        cvv = request.POST.get('cvv')
        donationAmount = request.POST.get('donationAmount')

        dn = Donation(name = name, email = email, address = address, city = city, 
        state = state, zipcode = zipcode, card_name = card_name, card_number=card_number,
        exp_month = exp_month, exp_year = exp_year, cvv = cvv, donationAmount = donationAmount)

        dn.save()
        messages.success(request,"Thank you for your donation")
        return redirect('donationSuccess')




    return render(request, 'donationPage.html')

@login_required(login_url='login')
def donationSuccess(request):
    return render(request,'donationSuccess.html')


def loginUser(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == "POST":
        username = request.POST['username'].lower()
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "Username does not exist")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # if the credentials are correct redirect user to profiles page
            return redirect(request.GET['next'] if 'next' in request.GET else 'profiles')
        else:
            messages.error(request, "Username or Password is incorrect")

    return render(request, "login_register.html")


def logoutUser(request):
    logout(request)
    messages.info(request, "User was logged out!")
    return redirect('login')


def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, "User account was created!")

            login(request, user)
            return redirect('profiles')
        else:
            messages.success(
                request, "An error has occurred during registration")

    context = {'page': page, 'form': form}
    return render(request, 'login_register.html', context)
