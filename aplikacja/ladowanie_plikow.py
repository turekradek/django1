import os
def handle_uploaded_file(f, title='plik1.txt'):
    sciezka = 'E:\\!!!!__programowanie__\\!!!___git_projekty\\django1\\pliki\\'
    with open(sciezka + title, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)