from django.shortcuts import render, redirect
from .forms import User_Creation_Form, UserUpdateForm, ProfileUpdateForm

def register(request):
    if request.method == 'POST':
        form = User_Creation_Form(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])  # Hachage du mot de passe
            user.save()
            return redirect('login')
    else:
        form =  User_Creation_Form()
    context =  {'form': form}
    return render(request, 'users/register.html', context)

def profile(request):
    context = {
        
    }
    return render(request, 'users/profile.html', context)


def profile_update(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'users/profile_update.html', context)

# Create your views here.
