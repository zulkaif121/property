from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from properties.models import PropertyImage,Property
from rest_framework.views import APIView
from properties.serializers import PropertySerializer


class ProperyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [AllowAny]  



    #def create(self, request, *args, **kwargs):

        #serializer = self.get_serializer(data=request.data)
        #if serializer.is_valid():
        #   user = serializer.save()
        #   token, created = Token.objects.get_or_create(user=user)  
        #    return Response({
        #        'user': CustomUserSerializer(user).data,
        #        'token': token.key 
        #    }, status=status.HTTP_201_CREATED)
        #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

