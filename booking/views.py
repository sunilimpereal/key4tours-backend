from django.shortcuts import render
from django.shortcuts import render
from django.test import tag
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from account import serializers
from booking.models import HolidayBooking
from booking.serializers import BookHolidayBookingSerializer, HolidayBookingSerializer, PersonSerializer, RoomSerializer
import stripe
# Create your views here.
stripe.api_key = "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"

# to get holiday details for home screen
class HolidayBookingView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request, uid, format=None):
        queryset = HolidayBooking.objects.filter(uid=uid)
        serializer = HolidayBookingSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, uid, format=None):
        serializer = BookHolidayBookingSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            holidayBooking = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostHolidayBookingView(APIView):
    # permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = BookHolidayBookingSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            holidayBooking = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CreatePaymentSessionView(APIView):
    def post(self, request, format=None):
        currency = request.data["currency"]
        product_name = request.data["product_name"]
        unit_amount = request.data["unit_amount"]
        quantity = request.data["quantity"]
        
        YOUR_DOMAIN = 'http://localhost:4242'
        try:
            checkout_session = stripe.checkout.Session.create(
                line_items=[{
                        'price_data': {
                            'currency': currency,
                            'product_data': {
                                'name':product_name ,
                            },
                        'unit_amount': unit_amount,
                        },
                        'quantity': quantity,
                        }
            ],
                mode='payment',
                payment_method_types=["card"],
                success_url=YOUR_DOMAIN + '/success.html',
                cancel_url=YOUR_DOMAIN + '/cancel.html',
            )
            response = {'session_id':checkout_session.id,'payment_intent':checkout_session.payment_intent,'session_url':checkout_session.url }
            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            response = {'session_error':str(e) }
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR )

    # return redirect(checkout_session.url, code=303)
        
class PaymentSessionSucessView(APIView):
    def get(self,request, bookingid,sessionid, format=None):
        holidayBookingObject = HolidayBooking.objects.filter(id=bookingid)
        holidayBookingObject.payment_id = sessionid
        holidayBookingObject.save()
        response = {'session_id':sessionid,'booking_id':bookingid }
        return Response(response, status=status.HTTP_200_OK)
        
        
        


class RoomView(APIView):
    def post(self, request, format=None):
        serializer = RoomSerializer(data=request.data,many=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PersonView(APIView):
    def post(self, request, format=None):
        serializer = PersonSerializer(data=request.data,many=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
