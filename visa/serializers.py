from multiprocessing import managers
from pyexpat import model
from statistics import mode
from unicodedata import category
from rest_framework import serializers
from package.models import Tag

from visa.models import Visa, VisaCategory


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = VisaCategory
        fields = [
            'id',
            'name',
            'description',
            'price',
            'visa',
        ]


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = [
            'id',
            'name',
            'description',
            'show_on_home', 
            ]


class VisaSerializer(serializers.ModelSerializer):
    price_categories = serializers.SerializerMethodField()
    tags = serializers.SerializerMethodField()
    @staticmethod
    def get_price_categories(self):
        all_cat = VisaCategory.objects.filter(visa=self.id)
        return CategorySerializer(all_cat, many=True).data
    @staticmethod
    def get_tags(self):
        if self.id is None:
            return None
        return TagSerializer(self.tags,many=True).data
    class Meta:
        model = Visa
        fields = [
            'id',
            'name',
            'documents_required',
            'description',
            'tags',
            'price_categories'
        ]


