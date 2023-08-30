"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
import statistics
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import staticfiles
from django.contrib import admin
from django.urls import path
from home.views import *
from vege.views import *

urlpatterns = [
    path("", home, name="home"),
    path("about/", about, name="about"),
    path("contact/", contact, name="contact"),


    path("receipes/", receipes, name="receipes"),
    path("delete-receipe/<id>/", delete_receipe, name="delete_receipe"),
    path("update-receipe/<id>/", update_receipe, name="update_receipe"),

    path("login/", login_page, name="login_page"),
    path("register/", register, name="register"),
    path("logout/", logout_page, name="logout_page"),

    path('students/',get_students, name="get_students"),



    path('admin/', admin.site.urls),
]

# this setting for to import media file like images
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
