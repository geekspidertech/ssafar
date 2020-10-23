from django.urls import path

from .views import SellerProfileDetails, SellerRequestList, sellerreg, approve_seller, reject_seller

urlpatterns = [
    #path('', views.sellerreg, name='sellerreg'),
    path('', sellerreg, name='sellerreg'),
    path('sellerrequestlist', SellerRequestList.as_view() , name='sellerrequestlist'),
    path('sellerdetails/<int:pk>', SellerProfileDetails.as_view() , name='sellerdetails'),
    path('reject_seller/<int:pk>', reject_seller, name='reject_seller'),
    path('approve_seller/<int:pk>', approve_seller, name='approve_seller'),
]

