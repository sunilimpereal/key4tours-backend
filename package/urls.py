from django.contrib import admin
from django.urls import path, include
from account.serializers import SendPasswordResetEmailSerializer
from package.views import AddSavedHolidayPackage, AmenitysView, DaysView, DurationView, HolidayPackageReviewView, HolidayPackageView, HolidayPackagesView, HomeTagHolidayPackagesView, HomeTagsView, ItineraryView, PostHolidayPackagesView, PriceCategoryView, RemoveSavedHolidayPackage, ReviewView, SavedHolidayPackage, SavedView, SearchRecommendationsView, SearchResultView, TagView
urlpatterns = [
    path('tags/', HomeTagsView.as_view(),name='tags'),
    path('tagHolidayPackages/<id>/', HomeTagHolidayPackagesView.as_view(),name='tagsHolidayPackage'),
    path('holidayPackages/<id>/', HolidayPackagesView.as_view(),name='holidayPackage'),
    path('postHolidayPackage', PostHolidayPackagesView.as_view(),name='postHolidayPackage'),
    path('holidayPackagesReview/<id>/', HolidayPackageReviewView.as_view(),name='holidayPackageReview'),
    path('holidayPackagesReview/', HolidayPackageReviewView.as_view(),name='holidayPackageReview'),
    #saved
    path('saved_holiday/<id>/', SavedHolidayPackage.as_view(),name='savedHoliday'),
    path('add_saved_holiday/<id>/<hid>/', AddSavedHolidayPackage.as_view(),name='add savedHoliday'),
    path('remove_saved_holiday/<id>/<hid>/', RemoveSavedHolidayPackage.as_view(),name='remove savedHoliday'),
    #search
    path('locations/', SearchRecommendationsView.as_view(),name='search recommendations'),
    path('search/', SearchResultView.as_view(),name='search result'),
    
    #db restoration
    path('all/amenity/', AmenitysView.as_view(),name='amenity'),
    path('all/days/', DaysView.as_view(),name='days'),
    path('all/duration/', DurationView.as_view(),name='amenity'),
    path('all/holidaypackage/', HolidayPackageView.as_view(),name='amenity'),
    path('all/itenary/', ItineraryView.as_view(),name='amenity'),
    path('all/pricecategory/', PriceCategoryView.as_view(),name='amenity'),
    path('all/review/', ReviewView.as_view(),name='amenity'),
    path('all/saved/', SavedView.as_view(),name='amenity'),
    path('all/tags/', TagView.as_view(),name='amenity'),

]
