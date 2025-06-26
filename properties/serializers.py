from rest_framework import serializers
from properties.models import Property, PropertyImage

class PropertyImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyImage
        fields = ['image', 'caption']


class PropertySerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    class Meta:
        model = Property
        fields = ['title', 'description', 'address', 'price', 'is_available', 'images']

    def get_images(self, obj):
        images = obj.images.all()  # uses related_name='images'
        return PropertyImageSerializer(images, many=True, context=self.context).data
