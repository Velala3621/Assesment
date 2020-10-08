from django.db import transaction
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from .forms import *
from .models import Product
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from django.utils.decorators import method_decorator

@method_decorator(login_required, name='dispatch')
class productlist(ListView):
    model = Product

@method_decorator(login_required, name='dispatch')
class ProfileCreate(CreateView):
    model = Product
    fields = ['title', 'description','image']


@method_decorator(login_required, name='dispatch')
class ProductItemCreate(CreateView):
    model = Product
    fields = ['title', 'description','image']
    success_url = reverse_lazy('product-list')

    def get_context_data(self, **kwargs):
        data = super(ProductItemCreate, self).get_context_data(**kwargs)
        if self.request.POST :
            data['Productitems'] = ProductItemFormset(self.request.POST)
            print(data['Productitems'])
        else:
            data['Productitems'] = ProductItemFormset()
        print(data)
        return data

    def form_valid(self, form):
        print("in form valid")
        context = self.get_context_data()
        Productitems = context['Productitems']
        with transaction.atomic():
            self.object=form.save()
            if Productitems.is_valid():
                Productitems.instance = self.object
                Productitems.save()
        return super(ProductItemCreate, self).form_valid(form)


class ProfileUpdate(UpdateView):
    model = Product
    success_url = '/'
    fields = ['title', 'description','image']


class ProductItemUpdate(UpdateView):
    model = Product
    fields = ['title', 'description','image']
    success_url = reverse_lazy('product-list')

    def get_context_data(self, **kwargs):
        data = super(ProductItemUpdate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['Productitems'] = ProductItemFormset(self.request.POST, instance=self.object)
        else:
            data['Productitems'] = ProductItemFormset(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        Productitems = context['Productitems']
        with transaction.atomic():
            self.object = form.save()
            if Productitems.is_valid():
                Productitems.instance = self.object
                Productitems.save()
        return super(ProductItemUpdate, self).form_valid(form)


class ProductDelete(DeleteView):
    model = Product
    success_url = reverse_lazy('product-list')

def UserRegistration(request):
    form=CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        user=form.save()
        user.set_password(user.password)
        user.save()
        return redirect("login")
    else:
        return render(request,'registration.html',{'form':form})

def loginview(request):
    if request.method == "POST":
        useR=request.POST.get("username")
        passworD=request.POST.get("password")
        x=authenticate(request,username=useR,password=passworD)
        if x is not None:
            login(request,x)
            return redirect("product-add")
        else:
            messages.info(request, "username or password is invalid")
    return render(request, 'registration/login.html')

