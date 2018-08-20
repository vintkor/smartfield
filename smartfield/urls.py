"""smartfield URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings

from .demo_view import DemoView
from .view import DashboardView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('demo/', DemoView.as_view()),
    path('dashboard/', include([
        path('', DashboardView.as_view(), name='dashboard'),
        path('planning/', include('planning.urls')),
        path('profile/', include('user_profile.urls')),
        path('reference-books/', include('reference_books.urls')),
    ])),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        re_path(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
