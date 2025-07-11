from django.urls import path, include
from rest_framework.routers import DefaultRouter
from properties.views import (
    PropertyViewSet, PropertyImageViewSet, PropertyAgentViewSet,
    PropertyReviewViewSet, PaymentMethodViewSet, BookingViewSet
)



app_name = 'properties'  # Add this line to specify the app's namespace

router = DefaultRouter()
router.register(r'properties', PropertyViewSet)
router.register(r'images', PropertyImageViewSet)
router.register(r'agents', PropertyAgentViewSet)
router.register(r'reviews', PropertyReviewViewSet)
router.register(r'payments', PaymentMethodViewSet)
router.register(r'bookings', BookingViewSet)

urlpatterns = [
    path('', include(router.urls)),

]
