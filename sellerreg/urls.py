from django.urls import path

from .views import SellerProfileDetails, SellerRequestList, sellerreg

urlpatterns = [
    #path('', views.sellerreg, name='sellerreg'),
    path('', sellerreg, name='sellerreg'),
    path('sellerrequestlist', SellerRequestList.as_view() , name='sellerrequestlist'),
    path('sellerdetails/<int:pk>', SellerProfileDetails.as_view() , name='sellerdetails'),
    

]

