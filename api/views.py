from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from .serializers import UserSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

User = get_user_model()

# Create your views here.

class RegisterView(generics.CreateAPIView):
    """
    API endpoint for user registration.
    
    Creates a new user account with the provided email and password.
    Returns the created user's details upon successful registration.
    
    Request body:
        - email: string (required)
        - password: string (required)
        - first_name: string (optional)
        - last_name: string (optional)
    """
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer

class UserProfileView(APIView):
    """
    API endpoint for retrieving user profile information.
    
    Requires authentication token in the request header.
    Returns the authenticated user's profile details.
    
    Response:
        - email: string
        - first_name: string
        - last_name: string
        - date_joined: datetime
    """
    permission_classes = (permissions.IsAuthenticated,)
    
    @swagger_auto_schema(
        operation_description="Get authenticated user's profile",
        responses={200: UserSerializer}
    )
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

class ProtectedView(APIView):
    """
    Protected API endpoint example.
    
    This endpoint demonstrates authentication protection.
    Only authenticated users can access this endpoint.
    
    Response:
        - message: string
        - user: string (user's email)
    """
    permission_classes = (permissions.IsAuthenticated,)
    
    @swagger_auto_schema(
        operation_description="Access protected endpoint",
        responses={
            200: openapi.Response(
                description="Success response",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'message': openapi.Schema(type=openapi.TYPE_STRING),
                        'user': openapi.Schema(type=openapi.TYPE_STRING),
                    }
                )
            )
        }
    )
    def get(self, request):
        return Response({
            "message": "You have access to this protected endpoint",
            "user": request.user.email
        })
