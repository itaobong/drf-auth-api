from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for User model.
    
    Handles user registration and profile data serialization.
    Includes password validation and confirmation functionality.
    
    Fields:
        - email: string (required) - User's email address
        - username: string (required) - User's username
        - password: string (required, write-only) - User's password
        - password2: string (required, write-only) - Password confirmation
        - first_name: string (required) - User's first name
        - last_name: string (required) - User's last name
    
    Validation:
        - Passwords must match
        - Password must meet Django's password validation requirements
        - Email must be unique
    """
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password],
        help_text="Required. Must meet Django's password validation rules."
    )
    password2 = serializers.CharField(
        write_only=True,
        required=True,
        help_text="Required. Must match the password field for confirmation."
    )

    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'password2', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True, 'help_text': "User's first name"},
            'last_name': {'required': True, 'help_text': "User's last name"},
            'email': {'help_text': "User's email address, must be unique"},
            'username': {'help_text': "User's username, must be unique"}
        }

    def validate(self, attrs):
        """
        Validate the password confirmation.
        
        Args:
            attrs (dict): Dictionary of field values
            
        Returns:
            dict: Validated data
            
        Raises:
            ValidationError: If passwords don't match
        """
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        """
        Create and return a new User instance.
        
        Args:
            validated_data (dict): Validated data from request
            
        Returns:
            User: Created user instance
        """
        validated_data.pop('password2')
        user = User.objects.create_user(**validated_data)
        return user
