from django.urls import path
from api.users.views import (
    BaseTokenObtainPairView,
    BaseTokenRefreshView,
    UserDetailView,
    UserRegisterView,
)

urlpatterns = [
    path("token/", BaseTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", BaseTokenRefreshView.as_view(), name="token_refresh"),
    path("register/", UserRegisterView.as_view(), name="register"),
    path("<int:pk>/", UserDetailView.as_view(), name="user"),
]
