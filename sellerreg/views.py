from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import CreateUserForm, SellerProfileForm
from django.views.generic import ListView , DetailView
from  . import models
from django.contrib.auth.decorators import login_required
from django.db import transaction



@login_required
@transaction.atomic
def sellerreg(request):
    username = request.user.get_username()
    staff_access= request.user.is_staff
    SellerReq= models.SellerProfile
    is_taken = SellerReq.objects.filter(seller_name__iexact=username).exists()
    if request.method == 'POST':
        form = SellerProfileForm(request.POST)
        if form.is_valid():
            #form.seller_name = username
            form.save()
            return redirect('home')
    else:
        
        form = SellerProfileForm(initial={'seller_name': username}) 
        
    return render(request, 'oscar/seller_reg/seller_registration.html', {
        'profile_form': form,'user':username, "is_taken" : is_taken,"show" :staff_access,
    })

class SellerProfileDetails(DetailView):
    model = models.SellerProfile
    template_name = 'oscar/seller_reg/seller_detail.html'
    
    
    
class SellerRequestList(ListView):
    model = models.SellerProfile
    template_name = 'oscar/seller_reg/seller_request_list.html'
    
    

    
#def approveseller(request):
#    if request.method == 'POST':
#        username = request.user.get_username()
#        if form.is_valid():
#            gst_number=form.cleaned_data.get('gst_number')
#            new_partner=Partner.objects.get_or_create(gst_number=gst_number, name=username)
#            return redirect('home')
#    else:
#        form = CreateUserForm()
#    return render(request, 'oscar/seller_reg/seller_detail.html'', {'created': false })

