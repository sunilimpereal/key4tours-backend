from django.shortcuts import render
from django.test import tag
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from package.serializers import PriceCategorySerializer

from visa.models import Tag, Visa, VisaCategory
from visa.serializers import CategorySerializer, TagSerializer, VisaSerializer
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


#------------------------------------------------------------------------------------------------------------
# get all data
#------------------------------------------------------------------------------------------------------------


class GetAllVisaView(APIView):
    def get(self,request,format=None):
        queryset = Visa.objects.all()
        serializer = VisaSerializer(queryset,many=True)
        return Response(serializer.data,status.HTTP_200_OK)
    def post(self, request,format=None):
        serializer = VisaSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"error":  str(serializer.error_messages) }, status=status.HTTP_400_BAD_REQUEST)

class GellAllTagVisaView(APIView):
    def get(self,request,format=None):
        queryset = Tag.objects.all()
        serializer = TagSerializer(queryset,many=True)
        return Response(serializer.data,status.HTTP_200_OK)
    def post(self, request,format=None):
        serializer = TagSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"error":  str(serializer.error_messages) }, status=status.HTTP_400_BAD_REQUEST)
class GetAllVisaCategoryView(APIView):
    def get(self,request,format=None):
        queryset = VisaCategory.objects.all()
        serializer = CategorySerializer(queryset,many=True)
        return Response(serializer.data,status.HTTP_200_OK)    
    def post(self, request,format=None):
        serializer = CategorySerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"error":  str(serializer.error_messages) }, status=status.HTTP_400_BAD_REQUEST)
    
    
    
    