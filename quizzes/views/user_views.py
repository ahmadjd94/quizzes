from django.contrib import messages
from django.shortcuts import redirect,render
from django.contrib.auth.forms import UserCreationForm


def register(request):
    if request.method == 'POST':
        f = UserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Account created successfully')
            return redirect('register')

    else:
        f = UserCreationForm()

    return render(request, 'registration/register.html', {'form': f})
