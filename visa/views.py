from django.shortcuts import render
from django.test import tag
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from visa.models import Tag, Visa
from visa.serializers import TagSerializer, VisaSerializer
# Create your views here.


class VisaView(APIView):
    def get(self,request,format=None):
        queryset = Visa.objects.all()
        serializer = VisaSerializer(queryset,many=True)
        return Response(serializer.data,status.HTTP_200_OK)

class VisaHomeTagView(APIView):
    def get(self,request,format=None):
        queryset = Tag.objects.all()
        serializer = TagSerializer(queryset,many=True)
        return Response(serializer.data,status.HTTP_200_OK)

class TagVisaView(APIView):
    def get(self,request,tagid,format=None):
        queryset = Visa.objects.filter(tags = tagid)
        serializer = VisaSerializer(queryset,many=True)
        return Response(serializer.data,status.HTTP_200_OK)


    
        