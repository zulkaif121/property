from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from properties.models import Property, PropertyImage, PropertyAgent, PropertyReview, PaymentMethod, Booking
from properties.serializers import (
    PropertySerializer, PropertyImageSerializer, PropertyAgentSerializer,
    PropertyReviewSerializer, PaymentMethodSerializer, BookingSerializer
)


class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [AllowAny]


class PropertyImageViewSet(viewsets.ModelViewSet):
    queryset = PropertyImage.objects.all()
    serializer_class = PropertyImageSerializer
    permission_classes = [AllowAny]


class PropertyAgentViewSet(viewsets.ModelViewSet):
    queryset = PropertyAgent.objects.all()
    serializer_class = PropertyAgentSerializer
    permission_classes = [AllowAny]


class PropertyReviewViewSet(viewsets.ModelViewSet):
    queryset = PropertyReview.objects.all()
    serializer_class = PropertyReviewSerializer
    permission_classes = [AllowAny]


class PaymentMethodViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = PaymentMethod.objects.filter(is_active=True)
    serializer_class = PaymentMethodSerializer
    permission_classes = [AllowAny]


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [AllowAny]

