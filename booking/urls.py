from django.contrib import admin
from django.urls import path, include
from account.serializers import SendPasswordResetEmailSerializer
from booking.views import CreatePaymentSessionView, HolidayBookingView, PaymentSessionSucessView, PostHolidayBookingView, RoomView
from package.views import HolidayPackageReviewView, HolidayPackagesView, HomeTagHolidayPackagesView, HomeTagsView
urlpatterns = [
    path('holidayBookings/<uid>/', HolidayBookingView.as_view(),name='holidayBookings'),
    path('postHolidayBooking', PostHolidayBookingView.as_view(),name='postholidayBookings'),
    path('postHolidayBooking/addroom/', RoomView.as_view(),name='hotelroom'),
    #payment success
    path('createpaymentSession', CreatePaymentSessionView.as_view() ,name='createpaymentSession'),
    path('paymentSuccessSession/<bookingid>/', PaymentSessionSucessView.as_view() ,name='paymentSuccessSession'),
 
   
   
    
]
