from django.urls import path, re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterView, UserProfileView, ProtectedView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

# Schema view for Swagger documentation
schema_view = get_schema_view(
    openapi.Info(
        title="DRF Authentication API",
        default_version='v1',
        description="A Django REST Framework API for user authentication and authorization",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # Swagger documentation endpoints
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # Authentication endpoints
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='register'),
    
    # Protected endpoints
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('protected/', ProtectedView.as_view(), name='protected'),
]
