from django.contrib import admin
from .models import Zawodnik , Ocena # 19 rejestracja modelu
# Register your models here.
##admin.site.register(Zawodnik)# 19 rejestracja modelu
# DRUGI SPOSÓB REJESTRACJI MODELU
@admin.register(Zawodnik)
class ZawodnikAdmin(admin.ModelAdmin):
    #fields = ['nazwisko','imie','wiek','pas','belki','email','fotka']
    #exclude = ['wiek']# wyłączenie wyświetlania
    list_display= ['nazwisko','imie','pas','belki','email','poczatek']# klikam Zawodniks i tam wyświetlone są  to co w liście
    list_filter = ('pas',)# lista filtrowania
    search_fields = ('pas',)# okienko wyszukiwania

admin.site.register(Ocena)



