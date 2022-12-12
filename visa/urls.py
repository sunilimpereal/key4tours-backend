from django.contrib import admin
from django.urls import path, include
from visa.views import GellAllTagVisaView, GetAllVisaCategoryView, GetAllVisaView, TagVisaView, VisaHomeTagView, VisaView
urlpatterns = [
    path('all', VisaView.as_view(), name='all Visa'),
    path('hometags', VisaHomeTagView.as_view(), name='VisaHomeTagView'),
    path('tagVisas/<tagid>', TagVisaView.as_view(), name='TagVisaView'),
    
    #=========================================================================
    # db backup
    #=========================================================================
    path('getAllVisa', GetAllVisaView.as_view(), name='allVisa'),
    path('getAllTagVisa', GellAllTagVisaView.as_view(), name='VisaTag'),
    path('getAllVisaCategory', GetAllVisaCategoryView.as_view(), name='visaCategory'),

]
