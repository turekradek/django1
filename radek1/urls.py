"""radek1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from aplikacja.views import test_response, nowy_zawodnik, edytuj, usuwanie
from django.conf import settings
from django.conf.urls.static import  static
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('aplikacja.urls')),# pod adresem zawodnik/ wczxytamy urls z aplikacji
    # zeby przejsc do test który jest w urls.py aplikacji trzeba najpierw wpisac zawodnik
    path('nowy/', nowy_zawodnik, name='nowy_zaw'),
    path('edytuj/<int:id>', edytuj, name='edytuj'),# <int:id> oznacza że trzeba dodac liczbe jako id
    path('usun/<int:id>', usuwanie, name='usun'),# <int:id> oznacza że trzeba dodac liczbe jako id
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(),name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)# DOPISANE W SETTINGS.PY MEDIA_URL I MEDIA_ROOT
