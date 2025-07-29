from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserForm

def register_view(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Change this to wherever you want to redirect
    else:
        form = CustomUserForm()
    return render(request, 'relationship_app/register.html', {'form': form})
