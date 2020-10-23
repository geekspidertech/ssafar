from django.contrib.auth import login, authenticate
from django.contrib.auth.models import Permission
from django.shortcuts import render, redirect
from .forms import CreateUserForm, SellerProfileForm
from django.views.generic import ListView , DetailView
from  . import models
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import render, get_object_or_404

from oscar.core.loading import get_model
from oscar.core.compat import get_user_model


User = get_user_model()
Partner = get_model('partner', 'Partner')

@login_required
@transaction.atomic
def sellerreg(request):
    username = request.user.get_username()
    staff_access= request.user.is_staff
    SellerReq= models.SellerProfile
    currentSeller = SellerReq.objects.filter(seller_name__iexact=username)
    is_taken = currentSeller.exists()
    if is_taken:
        req = get_object_or_404(models.SellerProfile, seller_name=username)
        is_approved = req.approved
        is_rejected = req.rejected
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
        "approved": is_approved, "rejected": is_rejected
    })

class SellerProfileDetails(DetailView):
    model = models.SellerProfile
    template_name = 'oscar/seller_reg/seller_detail.html'
    
    
    
class SellerRequestList(ListView):
    model = models.SellerProfile
    template_name = 'oscar/seller_reg/seller_request_list.html'


@login_required
@transaction.atomic
def approve_seller(request, pk):
    staff_access = request.user.is_staff
    seller_request = get_object_or_404(models.SellerProfile, id=pk)
    if staff_access:
        if request.method == 'POST':
            print ("seller approve request received")
            seller_request.approved = True
            seller_request.rejected = False
            seller_request.save()
            print (seller_request.approved)
            create_partner(pk, request.user.id)
            return render(request, 'oscar/seller_reg/seller_request_list.html', {
        'approval': "Approved"})
        else:
            return render(request, 'oscar/seller_reg/seller_request_list.html')
    return render(request, 'oscar/seller_reg/seller_request_list.html')

@login_required
@transaction.atomic
def reject_seller(request, pk):
    staff_access = request.user.is_staff
    seller_request = get_object_or_404(models.SellerProfile, id=pk)
    if staff_access:
        if request.method == 'POST':
            print ("seller delete request received")
            seller_request.approved = False
            seller_request.rejected = True
            seller_request.save()
            print (seller_request.rejected)
            return render(request, 'oscar/seller_reg/seller_registration.html', {
        'approval': "dispproved"})
        else:
            return render(request, 'oscar/seller_reg/seller_request_list.html')
    return render(request, 'oscar/seller_reg/seller_request_list.html')

def create_partner(seller_id, seller_user):
    print (seller_user)
    print (seller_id)
    SellerReq = get_object_or_404(models.SellerProfile, id=seller_id)
    #is_taken = SellerReq.objects.filter(seller_gst_number__iexact=username).exists()
    print (SellerReq)
    gst = SellerReq.gst_number
    title = SellerReq.seller_reg_title
    user = User.objects.get(username=SellerReq)
    print (user)
    new_partner = Partner.objects.get_or_create(gst_number=gst, name=title)
    thisPartner = get_object_or_404(Partner, gst_number=gst)
    thisPartner.users.add(user)
    dashboard_access_perm = Permission.objects.get(
        codename='dashboard_access', content_type__app_label='partner')
    user.user_permissions.add(dashboard_access_perm)
    thisPartner.save()
    print (thisPartner)
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

