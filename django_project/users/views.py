from django.shortcuts import render, redirect
from django.contrib import messages #for a one time message
from django.contrib.auth.decorators import login_required #login check to ensure that person can't see pages without logging in
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

def register(request):
    if request.method == 'POST': #if request is to register create form
        form = UserRegisterForm(request.POST)
        if form.is_valid(): # if form is valid obtain username into dictionary cleaned_data
            form.save() #save form
            username = form.cleaned_data.get('username')
            messages.success(request, f'You are now a member!')
            return redirect('login')
    else:
        form = UserRegisterForm() #else 
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)



#decorators add functonality to exisiting function
#in our case it prevents user from seeing profile without logging in


#different possible messages:
#messages.debug
#messages.success
#messages.warning
#messages.error
#messages.info