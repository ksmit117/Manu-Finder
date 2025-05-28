from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ToDoList, Item, Manufacturer, Product
from django.contrib.auth import authenticate, login
from .forms import LoginForm, SignupForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from .models import Manufacturer


def Tsearch_manu(request):
    return render(request, 'Tsearch_manu.html', {})

def test_search(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        manufacturer = Manufacturer.objects.filter(name__icontains=searched)  # Fixed filter
        return render(request, 'test_search.html', {'searched': searched, 'manufacturer': manufacturer})  # Fixed variable name
    else:
        return render(request, 'test_search.html', {})

def test_result(request):
    return render(request, 'test_result.html', {})
    

def index(response, id):
    ls = ToDoList.objects.get(id=id)
    return render(response, "main/base.html", {})

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def search_view(request):
    query = request.GET.get('q', '')  # Using GET is fine, but form needs to use GET method too
    results = []
    
    if query:
        results = Manufacturer.objects.filter(
        Q(name__icontains=query) | Q(location__icontains=query)
    )
    return render(request, 'search.html', {'results': results, 'query': query})
# The search function is now using the Manufacturer model to filter results based on the name field.    

def manufacturer_detail(request, manufacturer_id):
    manufacturer = Manufacturer.objects.get(id=manufacturer_id)
    products = manufacturer.product_set.all()  # Assuming a related Product model
    
    return render(request, 'manufacturer_detail.html', {
        'manufacturer': manufacturer,
        'products': products
    })
def test(request):
    return render(request, 'test.html')

def Manu(request):
    manufacturers = Manufacturer.objects.all()  # Get all manufacturers from database
    context = {
        'manufacturers': manufacturers
    }
    return render(request, 'Manu.html', context)

def profile(request):
    return HttpResponse('Profile page')

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignupForm()
    return render(request, 'sign_up.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to homepage after login
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)  # Log out the user
    return redirect('login')  # Redirect to login page after logout

def forgot_password_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        #Not fully implemented
        # Logic to send password reset email
        return HttpResponse('Password reset email sent')
    return render(request, 'forgot_password.html')

def profile_view(request):
    return render(request, 'profile.html')

def settings_view(request):
    return render(request, 'settings.html')

def contact_view(request):
    return render(request, 'contact.html')

def help_view(request):
    return render(request, 'help.html')






def z1(request):
    #if request.method == 'POST':
      #  form = SignupForm(request.POST)
        #if form.is_valid():
         #   user = form.save(commit=False)
        #    user.set_password(form.cleaned_data['password'])
       #     user.save()
      #      login(request, user)
     #       return redirect('home')
    #else:
        #form = SignupForm()
    return render(request, 'z1_redacted.html')  # Redirect to a different page for now

def redacted(request):
    #if request.method == 'POST':
       # form = LoginForm(request.POST)
        #if form.is_valid():
         #   username = form.cleaned_data['username']
          #  password = form.cleaned_data['password']
           # user = authenticate(username=username, password=password)
            #if user is not None:
             #  login(request, user)
              #  return redirect('home')
            #else:
             #   form.add_error(None, 'Invalid username or password')
    #else:
     #   form = LoginForm()
    return render(request, 'z_redacted.html')  # Redirect to a different page for now