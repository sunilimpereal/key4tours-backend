from django.contrib import admin
from django.urls import path, include
from visa.views import TagVisaView, VisaHomeTagView, VisaView
urlpatterns = [
    path('all', VisaView.as_view(), name='all Visa'),
    path('hometags', VisaHomeTagView.as_view(), name='VisaHomeTagView'),
    path('tagVisas/<tagid>', TagVisaView.as_view(), name='TagVisaView'),

]
