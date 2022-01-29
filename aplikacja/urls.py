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
from django.urls import path
from aplikacja.views import test_response, zawodnik, index_html , works_html, about_me_html, contact_html, components_html\
    , pasowanie_html, lista_zawodnikow_html, logowanie_html, nowy_zawodnik, upload_file, tresc_pliku, jakie_pliki

urlpatterns = [
    path('test/', test_response),
    path('zawodnik/', zawodnik, name='zawodnik'), # path( adres strony , jaka funkcja w views  ma byc wywolana
    path('glowna/', index_html, name='glowna_strona'),
    path('contact/', contact_html, name='kontakt'),
    path('works/', works_html, name='praca'),
    path('aboutme/', about_me_html, name='omnie'),
    path('components/', components_html, name='komponenty'),
    path('pasowanie/', pasowanie_html, name='pasowanie'),
    path('lista_zawodnikow/', lista_zawodnikow_html, name='lista_zawodnikow_'),
    path('logowanie/', logowanie_html, name='logowanie'),
    path('plik/', upload_file, name='nowy_plik'),
    path('nowy_zawodnik/', nowy_zawodnik, name='nowy_zawodnik'),
    path('jakie_pliki/', jakie_pliki, name='jakie_pliki'),
    path('tresc_pliku/<int:id>', tresc_pliku, name='tresc_pliku'),


]
