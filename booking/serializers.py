
from multiprocessing import managers
from pyexpat import model
from statistics import mode
from rest_framework import serializers
from account.models import User
from account.serializers import UserProfileSerializer
from booking.models import HolidayBooking, Person, Room
from package.serializers import DurationSerializer, PriceCategorySerializer


class HolidayBookingSerializer(serializers.ModelSerializer):
    rooms = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()
    selected_duration = serializers.SerializerMethodField()
    selected_category = serializers.SerializerMethodField()

    @staticmethod
    def get_rooms(self):
        if self.id is None:
            return None
        rooms = Room.objects.filter(holidayBooking=self.id)
        return RoomSerializer(rooms, many=True).data

    @staticmethod
    def get_user(self):
        if self.id is None:
            return None
        # user = User.objects.get(id=)
        return UserProfileSerializer(self.uid).data

    @staticmethod
    def get_selected_duration(self):
        if self.id is None:
            return None
        # user = User.objects.get(id=)
        return DurationSerializer(self.selected_duration).data

    @staticmethod
    def get_selected_category(self):
        if self.id is None:
            return None
        # user = User.objects.get(id=)
        return PriceCategorySerializer(self.selected_category).data

    class Meta:
        model = HolidayBooking
        fields = [
            'id',
            'number',
            'selected_duration',
            'selected_category',
            'rooms',
            'package_id',
            'user',
            'payment_id',
            'start_date',
            'end_date',
        ]


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = [
            'id',
            'gender',
            'first_name',
            'last_name',
            'dob',
            'passport_no',
        ]


class RoomSerializer(serializers.ModelSerializer):
    persons = PersonSerializer(many=True)
    class Meta:
        model = Room
        fields = [
            'id',
            'room_no',
            'holidayBooking',
            'persons'
        ]

    def create(self, validated_data):
        persons_data = validated_data.pop('persons')
        room = Room.objects.create(**validated_data)
        for person_data in persons_data:
            Person.objects.create(room=room, **person_data)
        return room


class BookHolidayBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = HolidayBooking
        fields = [
            'id',
            'number',
            'selected_duration',
            'selected_category',
            'package_id',
            'uid',
            'payment_id',
            'start_date',
            'end_date',
            'grand_total'
        ]
