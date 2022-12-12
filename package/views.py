from django.shortcuts import render
from django.test import tag
from numpy import save
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from account import serializers
from package.models import Amenity, Day, Duration, HolidayPackage, Itinerary, PriceCategory, Review, Saved, Tag

from package.serializers import AmenitiesSerializer, DaySerializer, DurationSerializer, HolidayPackageSearchSerializer, HolidayPackageSerializer, HomeTagHolidayPackageSerializer, HomeTagsSerializer, ItinerarySerializer, PriceCategorySerializer, ReviewSerializer, SavedSerializer
# Create your views here.


# to get tags for home screen
class HomeTagsView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        queryset = Tag.objects.all()
        serializer = HomeTagsSerializer(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

# to get tags for home screen


class HomeTagHolidayPackagesView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request, id, format=None):
        queryset = HolidayPackage.objects.filter(tags=Tag.objects.get(id=id))
        serializer = HomeTagHolidayPackageSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# to get holiday details for home screen


class HolidayPackagesView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request, id, format=None):
        queryset = HolidayPackage.objects.get(id=id)
        serializer = HolidayPackageSerializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request,format=None):
        serializer = HolidayPackageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"error": "failed to save holiday"}, status=status.HTTP_400_BAD_REQUEST)


class PostHolidayPackagesView(APIView):
    def post(self, request,format=None):
        serializer = HolidayPackageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"error": "failed to save holiday"  }, status=status.HTTP_400_BAD_REQUEST)
# to add and get review of a holiday package


class HolidayPackageReviewView(APIView):
    # permission_classes = [IsAuthenticated]
    def get(self, request, id, format=None):
        reviews = Review.objects.filter(package_id=id)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"error": "failed to post review"}, status=status.HTTP_400_BAD_REQUEST)


# -------------------------------------------------SAVED
# to get saved package and add package
class SavedHolidayPackage(APIView):
    # permission_classes = [IsAuthenticated]
    def get(self, request, id, format=None):
        saved = Saved.objects.get(uid=id)
        serializer = SavedSerializer(saved)
        return Response(serializer.data, status=status.HTTP_200_OK)


# to add a holiday to saved
class AddSavedHolidayPackage(APIView):
    # permission_classes = [IsAuthenticated]
    def get(self, request, id, hid, format=None):
        saved = Saved.objects.get(uid=id)
        saved.holiday_package.add(hid)
        serializer = SavedSerializer(saved)
        return Response(serializer.data, status=status.HTTP_200_OK)

# to delete a holiday from saved


class RemoveSavedHolidayPackage(APIView):
    # permission_classes = [IsAuthenticated]
    def get(self, request, id, hid, format=None):
        saved = Saved.objects.get(uid=id)
        saved.holiday_package.remove(hid)
        serializer = SavedSerializer(saved)
        return Response(serializer.data, status=status.HTTP_200_OK)

# ----------------------------------------------------------------------------SEARCH
# to GET search recomendations


class SearchRecommendationsView(APIView):
    # permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        package_locations = HolidayPackage.objects.values_list(
            'location', flat=True)
        package_country = HolidayPackage.objects.values_list(
            'country', flat=True)
        package_names = HolidayPackage.objects.values_list(
            'name', flat=True)
        return Response({
            "countries": package_country,
            "locations": package_locations,
            "name": package_names
        }, status=status.HTTP_200_OK)

# to GET search value


class SearchResultView(APIView):
    # permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        key    = request.GET['key']
        packages_ids   = HolidayPackage.objects.values_list(
            'id', flat=True)
        # serializer = HolidayPackageSearchSerializer(packages, many=True)
        return Response({
            "Search_Result":packages_ids 
            },status=status.HTTP_200_OK)
    
    

#--------------------------------------------------------------------------------------------------------------------------------------------
# to get all values for db restoring 
#--------------------------------------------------------------------------------------------------------------------------------------------

class AmenitysView(APIView):
    def get(self,request):
        queryset = Amenity.objects.all()
        serializer = AmenitiesSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request,format=None):
        serializer = AmenitiesSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"error":  str(serializer.error_messages) }, status=status.HTTP_400_BAD_REQUEST)

class DaysView(APIView):
    def get(self,request):
        queryset = Day.objects.all()
        serializer = DaySerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request,format=None):
        serializer = DaySerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"error": "failed to save day data"}, status=status.HTTP_400_BAD_REQUEST)


class DurationView(APIView):
    def get(self,request):
        queryset = Duration.objects.all()
        serializer = DurationSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request,format=None):
        serializer = DurationSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"error": "failed to save day data"}, status=status.HTTP_400_BAD_REQUEST)

class HolidayPackageView(APIView):
    def get(self,request):
        queryset = HolidayPackage.objects.all()
        serializer = HolidayPackageSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request,format=None):
        serializer = HolidayPackageSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"error": "failed to save day data"}, status=status.HTTP_400_BAD_REQUEST)
        

class ItineraryView(APIView):
    def get(self,request):
        queryset = Itinerary.objects.all()
        serializer = ItinerarySerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request,format=None):
        serializer = ItinerarySerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"error": "failed to save day data"}, status=status.HTTP_400_BAD_REQUEST)

class PriceCategoryView(APIView):
    def get(self,request):
        queryset = PriceCategory.objects.all()
        serializer = PriceCategorySerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request,format=None):
        serializer = PriceCategorySerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"error": "failed to save day data"}, status=status.HTTP_400_BAD_REQUEST)

class ReviewView(APIView):
    def get(self,request):
        queryset = Review.objects.all()
        serializer = ReviewSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request,format=None):
        serializer = ReviewSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"error": "failed to save day data"}, status=status.HTTP_400_BAD_REQUEST)


class SavedView(APIView):
    def get(self,request):
        queryset = Saved.objects.all()
        serializer = SavedSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request,format=None):
        serializer = SavedSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"error": "failed to save day data"}, status=status.HTTP_400_BAD_REQUEST)
        
class TagView(APIView):
    def get(self,request):
        queryset = Tag.objects.all()
        serializer = HomeTagHolidayPackageSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request,format=None):
        serializer = HomeTagHolidayPackageSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"error": "failed to save saved data"}, status=status.HTTP_400_BAD_REQUEST)