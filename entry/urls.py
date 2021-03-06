"""gwq URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url, include

# Django Admin
from django.contrib import admin

# REST Framework
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token

# Modules
from dictionary.views import DictionaryViewSet
from common.views import UserViewSet, GroupViewSet


schema_view = get_swagger_view(title='API Reference')

router = routers.DefaultRouter()
router.register(r'dictionaries', DictionaryViewSet)
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)

urlpatterns = [
    url('api/', include(router.urls)),
    # url(r'^api/users/current', current_user),
    path('admin/', admin.site.urls),
    url(r'^doc/$', schema_view),
    url(r'^api/token/auth', obtain_jwt_token),
    url(r'^api/token/refresh', refresh_jwt_token),
    url(r'^api/token/verify', verify_jwt_token),
    url(r'^api/auth', include('rest_framework.urls', namespace='rest_framework'))
]