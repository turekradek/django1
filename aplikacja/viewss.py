from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Zawodnik, Ocena
from .forms import ZawodnikForm , OcenaForm, UploadFileForm, SubscribeForm
from django.contrib.auth.decorators import login_required
import os, sys

from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm, TrescPlikuFrom
# Imaginary function to handle an uploaded file.
from .ladowanie_plikow import handle_uploaded_file
from .przerabianie_plikow import przerabianie
from radek1.settings import EMAIL_HOST_USER
from . import forms
from django.core.mail import send_mail
# Create your views here.
def test_response(request):
    # return HttpResponse('<h1>to jest nasz 1 test </h1>')
    #test = 'to jest wewnatrz views '#1
    # teraz przekazanie jakichś nazwisk
    zawodnicy = ['Turek','Radek']
    #return render(request , 'probny1.html',{'text':test}  )# 1 # zamiast linijki powyżej
    #return render(request, 'probny1.html', {'zmienna': ['Turek','Radek'] } )  # 1 # zamiast linijki powyżej
    # 3
    wszyscy = Zawodnik.objects.all()
    return render( request,'probny1.html', {'zmienna' : wszyscy } )

def zawodnik(request):
    # return HttpResponse('<h1>to jest nasz 1 test </h1>')
    return render(request , 'probny2.html')# zamiast linijki powyżej

def index_html( request ):
    return render(request, 'index.html')

def works_html( request ):
    return render(request, 'works.html')

def about_me_html( request ):
    return render(request, 'about.html')

def contact_html( request ):
    return render(request, 'contact.html')

def components_html( request ):
    return render(request, 'components.html')

@login_required
def pasowanie_html( request ):
    return render(request, 'pasowanie.html')
@login_required
def lista_zawodnikow_html( request ):
    fighters = Zawodnik.objects.all()
    return render(request, 'lista_zawodnikow.html', {'zawodnicy': fighters })

def logowanie_html( request ):
    return render(request, 'log_in.html')
@login_required
def nowy_zawodnik( request ):
    form3 = ZawodnikForm( request.POST or None , request.FILES or None)
    form3_ocena = OcenaForm( request.POST or None )# dodanie kolejnego form do nowego zawodnika

    if all(( form3.is_valid() , form3_ocena.is_valid()) ):# all() dodane dla wielu forms BYLO for3.is_valid()
        # BĘDZIE BŁĄD JEŚLI NIE DODAMY NAWIASÓW TAK ABY ALL PRZYJMOWAŁ TYLKO JEDEN ARGUMENT
        zawodnik = form3.save(commit=False)# przypisanie zamiast form3.save() commit oznacza ze
        # jeszcze nie zaaplikujemy do bazy dancy
        ocena = form3_ocena.save(commit=False)
        zawodnik.ranking = ocena# do cechy zawodnika ocena dodajemy ocene zapisana
        zawodnik.save()
        return redirect(lista_zawodnikow_html)  # przekierowanie do funkcji redirect trzeba zaimportowac

    return render( request, 'nowy_zawodnik.html', {'form3':form3, 'form3_ocena': form3_ocena})

@login_required
def edytuj( request, id ):
    zawodnik = get_object_or_404(Zawodnik, pk=id)
    oceny = Ocena.objects.filter(zawodnik=zawodnik)
    form3 = ZawodnikForm(request.POST or None, request.FILES or None, instance=zawodnik)# instance wypełni pola zwiazane z tym id
    #form3_ocena = OcenaForm(request.POST or None,  instance=dodatkowe)# instance wypełni pola zwiazane z tym id

    if form3.is_valid():
        form3.save()
        return redirect(lista_zawodnikow_html)# przekierowanie do funkcji redirect trzeba zaimportowac

    return render(request, 'edytuj_zawodnik.html', {'form3': form3, 'oceny':oceny})

@login_required
def usuwanie( request, id ):
    zawodnik = get_object_or_404(Zawodnik, pk=id)
    if request.method == 'POST':
        zawodnik.delete()
        return redirect(lista_zawodnikow_html)
    return render(request, 'potwierdz_usuwanie.html', {'zawodnik': zawodnik})

@login_required
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES )
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'],str(request.FILES['file']))
            # return HttpResponseRedirect('pasowanie_thanks.html')
            return render(request,'pasowanie_thanks.html')
    else:
        form = UploadFileForm()
    return render(request, 'nowy_plik.html', {'form': form})

def jakie_pliki(request):
    pliki = r'pliki'
    lista = os.listdir(pliki)
    slownik = { i: lista[i] for i in range(len(lista))}
    plik = open(os.path.join(pliki,lista[0]),'r',encoding='utf8')
    return render(request, 'jakie_pliki.html', {'slownik': slownik })

def tresc_pliku(request, id=-1):
    pliki = r'pliki'
    lista = os.listdir(pliki)
    slownik = { i: lista[i] for i in range(len(lista))}
    plik = open(os.path.join(pliki,lista[id]),'r',encoding='utf8')
    return render(request, 'tresc_pliku.html', {'plik': plik })

# Create your views here.
#DataFlair #Send Email
def subscribe(request):
    sub = forms.SubscribeForm()
    if request.method == 'POST':
        sub = forms.Subscribe(request.POST)
        subject = 'Welcome to DataFlair'
        message = 'Hope you are enjoying your Django Tutorials'
        recepient = str(sub['Email'].value())
        send_mail(subject,

            message, EMAIL_HOST_USER, [recepient], fail_silently = False)
        return render(request, 'email_thanks.html', {'recepient': recepient})
    return render(request, 'subscribe/index.html', {'form':sub})
