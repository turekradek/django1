from django.db import models
from PIL import Image
# Create your models here.


class Zawodnik(models.Model):
    BELTS = [
        ('BIAŁY', 'BIAŁY'),
        ('NIEBIESKI', 'NIEBIESKI'),
        ('PURPURA', 'PURPURA'),
        ('BRĄZOWY', 'BRĄZOWY'),
        ('CZARNY', 'CZARNY'),
    ]
    BELKI = [
        (0, '0'),
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
    ]
    nazwisko = models.CharField(max_length=50, blank=False)
    imie = models.CharField(max_length=50 , blank=False )
    wiek = models.PositiveSmallIntegerField(default=18)
    pas = models.CharField( max_length=20, default='BIAŁY', blank=False , choices=BELTS)
    belki = models.PositiveSmallIntegerField( default=0 , choices=BELKI)
    email = models.EmailField( unique=True , blank=True)
    poczatek = models.DateField(null=True, blank=True)
    # ranking = models.DecimalField( max_digits=5, decimal_places=2)
    fotka = models.ImageField(upload_to='fotki', null=True, blank=True)
    # plik = models.FileField

    def __str__(self):
        return self.nazwisko_i_imie()

    def nazwisko_i_imie(self):
        return "{} {}".format(self.nazwisko, self.imie)

class Ocena(models.Model):
    punkty = [
        (0, '0'),
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (6, '5'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10'),
    ]
    uzasadnienie = models.TextField( default='', blank=True)
    ranking = models.PositiveSmallIntegerField(default=10, choices=punkty)
    zawodnik = models.ForeignKey(Zawodnik, on_delete=models.CASCADE)
    # ForeignKey to one to many