"""ex1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from app import views

urlpatterns = [
    path('', views.cursos),
    path('<int:guid>/', views.curso_details),
    path('admin/', admin.site.urls),
    path('by_grau/', views.by_grau, name='by_grau'),
    path('by_depart/', views.by_depart, name='by_depart'),
    path('by_area/', views.by_area, name='by_area'),
    path('by_local/', views.by_local, name='by_local'),
    path('departs/', views.departamentos, name='departs'),
    path('areas/', views.areas, name='areas'),
    path('locais/', views.locais, name='locais'),
]
