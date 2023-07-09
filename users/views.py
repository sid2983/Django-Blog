from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.urls import reverse
from django.contrib import messages
from .forms import UserRegistrationForm,EditProfileForm,EditUserForm
from django.contrib.auth.decorators import login_required
from users.models import User,Profile
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin


def register(request):
    if request.method == 'POST':
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return HttpResponseRedirect(reverse('djblog:djblog-home'))

    else:
        form=UserRegistrationForm()
    return render(request, 'users/register.html',{'form':form})
    

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request,data=request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username=username,password=password)

                if user is not None:
                    if user.is_active:
                        login(request,user)
                        return HttpResponseRedirect(reverse('djblog:djblog-home'))
                    else:
                        return HttpResponse('USER IS NOT ACTIVE!!')
                    
        else:
            form = AuthenticationForm()
        return render(request,'users/login.html',{'form':form})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('djblog:djblog-home'))


class UserProfileCreate(LoginRequiredMixin,CreateView):
    model = Profile
    template_name = 'users/create_profile.html'
    fields = ['portfolio','profile_pic']
    



    def form_valid(self,form):
        form.instance.user = self.request.user

        return super().form_valid(form)


def user_profile(request):
    if request.user.is_authenticated:
        
        
        if request.method =='POST':
            fm = EditUserForm(request.POST,instance=request.user)
            fm2 = EditProfileForm(request.POST,request.FILES,instance=request.user.profile)
            if fm.is_valid() and fm2.is_valid():
                fm.save()
                fm2.save()
        else:
            fm = EditUserForm(instance=request.user)
            fm2 = EditProfileForm(instance=request.user.profile)
        return render(request,'users/profile.html',{'name':request.user,'Uform':fm,'Pform':fm2})
    else:
        return HttpResponseRedirect(reverse('user_login'))