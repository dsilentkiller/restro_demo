

from django.views.generic import CreateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate 
from user.forms import RegistrationForm 
from django.contrib.auth.decorators import login_required

######################## table ###########################


# class LoginView(LoginView):
#     model = User
#     template_name = 'user/login.html'
#     success_url = reverse_lazy('order:order_create')

# class RegisterView(LoginView):
#     model = User
#     template_name = 'user/login.html'
#     success_url = reverse_lazy('order:order_create')
# class TableDetailView(DetailView):
#     model = Table
#     template_name = 'item/item_detail.html'
#     success_url = reverse_lazy('order:item_list')


# ================================================order -============================================================================
def sign_up(request):
    # form =RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('/app/inventory/list/')
        else:
            form = RegisterForm()
    # context ={'form':form}

    return render(request,'registration/register.html' ,{'form':form})