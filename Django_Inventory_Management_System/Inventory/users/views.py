from django.shortcuts import render, redirect
from  django.contrib.auth.forms import  UserCreationForm
from .forms import User_Creation_Form

def register(request):
    if request.method == 'POST':
        form = User_Creation_Form(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])  # Hachage du mot de passe
            user.save()
            return redirect('dashboards-index')
    else:
        form =  User_Creation_Form()
    context =  {'form': form}
    return render(request, 'users/register.html', context)



# Create your views here.
