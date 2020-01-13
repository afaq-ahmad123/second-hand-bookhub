from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import profileEditForm

# Create your views here.
from django.apps import apps
userInfo = apps.get_model('login','user')
def prof(request):
    if 'email' in request.session:
        email = request.session['email']
        user = userInfo.objects.get(email=email)
        return render(request,'user/profile.html', {'user': user})
    else:
        return redirect("login")

def edit(request):
    return render(request,'user/edit.html')


def editUserProfile(request):
        email = request.session["email"]
        user = userInfo.objects.get(email=email)
        if request.method == "POST":
            print("in post")
            form = profileEditForm(request.POST, request.FILES, instance=user)
            if form.is_valid():
                form.save()
                messages.success(request, f'Profile Information Successfully Updated!')
                return redirect(editUserProfile)
            else:
                messages.success(request, f'Could not update.Please fill all the fields!')
                form = profileEditForm(instance=user)
                return render(request, 'user/edit.html', {'user': user, 'form': form})

        else:
            print("in else")
            form = profileEditForm(instance=user)
            return render(request, 'user/edit.html', {'user': user, 'form': form})