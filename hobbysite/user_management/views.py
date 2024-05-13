from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile
from .forms import ProfileForm

@login_required
def update_profile(request):
    # if request.method == 'POST':
    #     form = ProfileForm(request.POST, instance=request.user.profile)
    # try:
    #     profile = request.user.profile
    # except Profile.DoesNotExist:
    #     profile = Profile(user=request.user)
    #     profile.save()

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('user_management:profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = ProfileForm(instance=request.user.profile)
        # form = ProfileForm(instance=profile)
    return render(request, 'user_management/profile.html', {'form': form})