from django.urls import path
from .api_views import UserListApi


urlpatterns = [
    path('user', UserListApi.as_view()),
]
