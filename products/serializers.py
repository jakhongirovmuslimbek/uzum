from rest_framework import serializers
from . import models

class CategorySerializer(serializers.ModelSerializer):
    thumbnail_image = serializers.ImageField(read_only=True)

    class Meta:
        model = models.Category
        fields = "__all__"
    

class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SubCategory
        fields = "__all__"
    

