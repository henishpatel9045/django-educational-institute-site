"""classes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from mainpage import views
from django.conf.urls.static import static
 
urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('course/', views.all_course, name='course'),
    path('courses/', include('course.urls')),
    path('contact/', views.contact, name='contact'),
    path('about/', views.aboutus, name='about'),
    path('admin/', admin.site.urls, name='admin'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    