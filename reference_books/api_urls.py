from django.urls import path
from .api_views import UserListApi


urlpatterns = [
    path('', UserListApi.as_view()),
]
