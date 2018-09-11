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
from django.conf.urls.static import static
from rest_framework import permissions
from rest_framework_jwt.views import obtain_jwt_token
from .demo_view import DemoView
from .view import DashboardView
from user_profile import api_views
from rest_framework_swagger.views import get_swagger_view

from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="SmartField API",
      default_version='v1',
      description="Test API",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="alkv84@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   validators=['flex', 'ssv'],
   public=True,
   permission_classes=(permissions.IsAuthenticated,),
)


# schema_view = get_swagger_view(title='SmartField API Docs')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('demo/', DemoView.as_view()),
    path('dashboard/', include([
        path('', DashboardView.as_view(), name='dashboard'),
        path('planning/', include('planning.urls')),
        path('profile/', include('user_profile.urls')),
        path('reference-books/', include('reference_books.urls')),
    ])),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt')),
    # path('api/v1/', include([
    #     path('', schema_view),
    #     path('user-profiles/', include('user_profile.api_urls')),
    #     path('reference-books/', include('reference_books.api_urls')),
    # ])),
    re_path(r'^', include('drf_autodocs.urls')),
    # path('api-v1', schema_view),
    # re_path(r'^api_docs/swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    # re_path(r'^api_docs/swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^api_docs/redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api-v1_user-profiles/', include('user_profile.api_urls')),
    path('api-v1_reference-books/', include('reference_books.api_urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        re_path(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
