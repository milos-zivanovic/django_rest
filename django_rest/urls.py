"""django_rest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def project_root(request):
    return Response({app: request.build_absolute_uri(f'/{app}/') for app in settings.CUSTOM_APPS})


urlpatterns = [
    # Project Root
    path('', project_root),

    # Admin Panel
    path('admin/', admin.site.urls),

    # Login/Logout for Browsable API
    path('api-auth/', include('rest_framework.urls')),

    # Quickstart App Routes
    path('quickstart/', include('quickstart.urls')),

    # Snippets App Routes
    path('snippets/', include('snippets.urls')),
]
