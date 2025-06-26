from django.urls import path, include
from rest_framework.routers import DefaultRouter
from accounts.views import CustomUserViewSet, LoginView,UserProfileView



app_name = 'accounts'  # Add this line to specify the app's namespace

router = DefaultRouter()
router.register(r'users', CustomUserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/',UserProfileView.as_view(),name="user-profile")
]
