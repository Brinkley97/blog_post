from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from accounts.forms import MyRegistrationForm
from django.contrib.auth import login, logout

# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        form = MyRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('accounts:testing')
    else:
        form = MyRegistrationForm()
    return render(request, 'accounts/signup.html', {'form': form})

def testing_view(request):
    return render(request, 'accounts/testing.html')
