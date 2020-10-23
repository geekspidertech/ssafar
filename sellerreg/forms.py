from django.contrib.auth.forms import UserCreationForm
from django import forms
#from crispy_forms.helper import FormHelper
#from crispy_forms.layout import Layout, Fieldset, Field
from  . import models
# from django.contrib.auth.models import User
from oscar.core.compat import get_user_model
from oscar.core.loading import get_model

   
class CreateUserForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        UserAddress = get_model('address', 'UserAddress')
        fields=['username', 'email', 'is_staff','password1', 'password2']

#class sellerdetails(UserCreationForm):
#    class Meta:
#        model = Partner
#        fields=[ 'gst_number']

class SellerProfileForm(forms.ModelForm):
    #seller_name = forms.CharField(disabled=True)
    
    class Meta:
        model = models.SellerProfile
        fields = ('seller_name', 'seller_reg_title','email_id','bio','gst_number','phone_number','state','city')
        widgets = {'seller_name': forms.HiddenInput()}
   
        