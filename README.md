# transbot-wykop
Bot tłumaczący artykuły z wykop.pl przy pomocy translatora deepl.com napisany w Pythonie. Docelowo będzie dodawał komentarz z tłumaczeniem pod wykopem.

Jest to bardzo wczesna wersja, powiedzmy `v0.0.1`. Zrobiony z zajawki, na razie ma bardzo ograniczoną funkcjonalność. Jeżeli się przyjmie to będę go rozwijał, zapraszam też do wystawiania PR.

## Algorytm
(wszystko w `5` minutowej pętli)
1. Pobranie najnowszych linków z API wykopu ([wykop-sdk](https://github.com/p1c2u/wykop-sdk))
1. Wyfiltrowanie potencjalnie dających się przetłumaczyć artykułów (ignorowanie domeny `.pl` oraz niektórych domen)
1. Dla każdego linku
    1. Otworzenie go przeglądarce oraz wczytanie kodu html ([selenium](https://github.com/SeleniumHQ/selenium) + [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/))
    1. Wyekstrachowanie i skopiowanie treści artykułu ([newspaper3k](https://github.com/codelucas/newspaper))
    1. Otworzenie tłumacza DeepL w przeglądarce
    1. Wklejenie artykułu do tłumacza
    1. Wykrycie języka artykułu - jeżli jest w języku polskim, zaprzestanie kontynuowania
    1. Wystawienie komentarza z tłumaczeniem na wykopie
    
## Wymagania
- Python 3
- [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/)

## Instalacja i uruchomienie
Utworzenie pliku `config.yaml` korzystając z [example.config.yaml](https://github.com/burnoo/transbot-wykop/blob/master/example.config.yaml)
A następnie:
```bash
pip3 install -r requirements.txt
python3 app.py
```
