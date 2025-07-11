from rest_framework import serializers
from properties.models import Property, PropertyImage, PropertyAgent, PropertyReview, PaymentMethod, Booking

class PropertyImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyImage
        fields = ['id', 'image', 'caption', 'uploaded_at']

class PropertyAgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyAgent
        fields = ['id', 'name', 'email', 'phone', 'properties', 'created_at', 'updated_at']

class PropertyReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyReview
        fields = ['id', 'property', 'user_name', 'rating', 'comment', 'created_at', 'updated_at']

class PaymentMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMethod
        fields = ['id', 'name', 'description', 'is_active', 'created_at', 'updated_at']

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'property', 'user_name', 'user_email', 'user_phone', 'guests', 'check_in_date', 'check_out_date']

class PropertySerializer(serializers.ModelSerializer):
    images = PropertyImageSerializer(many=True, read_only=True)
    agents = PropertyAgentSerializer(many=True, read_only=True)
    reviews = PropertyReviewSerializer(many=True, read_only=True)
    bookings = BookingSerializer(many=True, read_only=True)

    class Meta:
        model = Property
        fields = [
            'id', 'title', 'description', 'address', 'price', 'currency', 'room_booking', 'total_rooms', 'room_price',
            'is_available', 'available_from', 'available_to', 'guests', 'pet_friendly', 'children', 'location',
            'overview', 'features', 'created_at', 'updated_at', 'images', 'agents', 'reviews', 'bookings'
        ]
