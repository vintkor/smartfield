from django.urls import path
from .views import (
    AuthView,
    user_logout,
)


app_name = 'user'
urlpatterns = [
    path('login/', AuthView.as_view(), name='login'),
    path('logout/', user_logout, name='logout'),
]
