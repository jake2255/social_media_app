from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register(request):
    """Register new user"""
    if request.method != 'POST':
        # Blank form
        form = UserCreationForm()
    else:
        # Process form
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect('social_media:index')
        
    # Display blank/invalid form
    return render(request, 'registration/register.html', {'form': form})