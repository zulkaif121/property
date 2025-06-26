from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from accounts.models import CustomUser
from accounts.serializers import CustomUserSerializer,UserProfileSerializer
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [AllowAny]  

    def create(self, request, *args, **kwargs):
        """
        Override the default create method to allow new users to sign up.
        """
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)  
            return Response({
                'user': CustomUserSerializer(user).data,
                'token': token.key 
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserProfileView(APIView):
    """
    Get the currently authenticated user's profile data.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user  # authenticated user from token
        serializer = UserProfileSerializer(user)
        return Response(serializer.data)



class LoginView(APIView):
    """
    User login view to authenticate and return token.
    """
    permission_classes = [AllowAny] 
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')

        if not email or not password:
            return Response({"detail": "Email and password are required"}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(request, email=email, password=password)  # use email here

        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        else:
            return Response({"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)