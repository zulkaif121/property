from django.urls import path, include
from rest_framework.routers import DefaultRouter
from properties.views import ProperyViewSet



app_name = 'properties'  # Add this line to specify the app's namespace

router = DefaultRouter()
router.register(r'', ProperyViewSet)

urlpatterns = [
    path('', include(router.urls)),

]
