from django.shortcuts import get_object_or_404
from drf_spectacular.utils import OpenApiExample, extend_schema, extend_schema_view
from rest_framework import generics, mixins, permissions
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from api.users.serializers import UserSerializer
from api.users.models import User


@extend_schema_view(
    post=extend_schema(tags=["auth"]),
)
class BaseTokenObtainPairView(TokenObtainPairView):
    pass


@extend_schema_view(
    post=extend_schema(tags=["auth"]),
)
class BaseTokenRefreshView(TokenRefreshView):
    pass


@extend_schema(
    tags=["auth"],
    request=UserSerializer,
    responses={201: UserSerializer},
    description="Register a new user.",
    examples=[
        OpenApiExample(
            "Example request",
            value={
                "first_name": "John",
                "last_name": "Doe",
                "email": "john.doe@example.com",
                "phone": "+1234567890",
                "password": "password123",
            },
            request_only=True,
        ),
        OpenApiExample(
            "Example response",
            value={
                "id": 1,
                "first_name": "John",
                "last_name": "Doe",
                "email": "john.doe@gmail.com",
                "phone": "+1234567890",
            },
            response_only=True,
        ),
    ],
)
class UserRegisterView(generics.CreateAPIView):
    """
    Custom user registration view.
    This view is used to register a new user.
    The user profile data is returned in the response.
    The user profile data includes the user's first name, last name, email, and phone number.
    """

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]


@extend_schema_view(
    get=extend_schema(
        tags=["users"],
        responses={200: UserSerializer(many=True)},
        description="Retrieve a user's profile.",
        examples=[
            OpenApiExample(
                "Example response",
                value=[
                    {
                        "id": 1,
                        "first_name": "John",
                        "last_name": "Doe",
                        "email": "john.doe@example.com",
                        "phone": "+1234567890",
                    }
                ],
                response_only=True,
            )
        ],
    ),
    put=extend_schema(
        tags=["users"],
        request=UserSerializer,
        responses={200: UserSerializer},
        description="Update a user's profile.",
        examples=[
            OpenApiExample(
                "Example request",
                value={
                    "first_name": "John",
                    "last_name": "Doe",
                    "email": "john.doe@example.com",
                    "phone": "+1234567890",
                },
                request_only=True,
            ),
            OpenApiExample(
                "Example response",
                value={
                    "id": 1,
                    "first_name": "John",
                    "last_name": "Doe",
                    "email": "john.doe@example.com",
                    "phone": "+1234567890",
                },
                response_only=True,
            ),
        ],
    ),
    patch=extend_schema(
        tags=["users"],
        request=UserSerializer,
        responses={200: UserSerializer},
        description="Partially update a user's profile.",
        examples=[
            OpenApiExample(
                "Example request",
                value={"first_name": "John"},
                request_only=True,
            ),
            OpenApiExample(
                "Example response",
                value={
                    "id": 1,
                    "first_name": "John",
                    "last_name": "Doe",
                    "email": "john.doe@example.com",
                    "phone": "+1234567890",
                },
                response_only=True,
            ),
        ],
    ),
    delete=extend_schema(
        tags=["users"],
        responses={204: None},
        description="Deactivate a user's profile.",
    ),
)
class UserDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView,
):
    """
    Custom user detail view.
    This view is used to retrieve, update, partially update, and deactivate a user's profile.
    The user profile data is returned in the response.
    The user profile data includes the user's first name, last name, email, and phone number.
    """

    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return User.objects.filter(is_active=True)

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, pk=self.kwargs["pk"])
        return obj

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
