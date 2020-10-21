from django.contrib import messages, auth
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import viewsets
from rest_framework.response import Response
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, request
from django.views.generic.base import View
from rest_framework.views import APIView
from .serializers import UesrSerializer
from .models import Userinfo
from django.views.generic import DetailView, ListView
from .forms import userregisterform, userupdateform
from django.views.generic.edit import FormView

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


def applyuser(request):
    if request.method == 'POST':
        form = userregisterform(request.POST, request.FILES)
        if form.is_valid():
            # file is saved
            form.save()
            return HttpResponseRedirect('success')
    else:
        form = userregisterform()
    return render(request, 'registration.html', {'form': form})


@login_required
def user_update(request):
    if request.method == 'POST':
        form = userupdateform(request.POST, instance=request.user)
        profile_form = userupdateform(request.POST, request.FILES, instance=request.user.userprofile) 
        if form.is_valid() and profile_form.is_valid():
            user_form = form.save()
            custom_form = profile_form.save(False)
            custom_form.user = user_form
            custom_form.save()
            return redirect('accounts:view_profile')
    else:
        form = EditProfileForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.userprofile)
        args = {}
        # args.update(csrf(request))
        args['form'] = form
        args['profile_form'] = profile_form
        return render(request, 'accounts/edit_profile.html', args)


def user_delete(request, pk):
    userin= get_object_or_404(Userinfo,pk=pk)
    if request.method=='POST':
        userin.delete()
        return redirect('success')
    return render(request, 'userdelete.html', {'object':userin})






def login(request):
    if request.user.is_authenticated():
        return redirect('success')

    if request.method == 'POST':
        email = request.POST.get('email_add')
        password = request.POST.get('password')
        user = auth.authenticate(username=email, password=password)

        if user is not None:
            # correct username and password login the user
            auth.login(request, user)
            return redirect('user_details')

        else:
            messages.error(request, 'Error wrong username/password')

    return render(request, 'login.html')



def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("success")


class user_detail(DetailView):
    model = Userinfo

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['user_detail'] = Userinfo.objects.all()
        return context
