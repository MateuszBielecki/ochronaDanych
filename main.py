def szyfr_cezara(wiadomosc, klucz, tryb="szyfrowanie"):
    wynik = ""
    for znak in wiadomosc:
        if znak.isalpha():
            przesuniecie = klucz if tryb == "szyfrowanie" else -klucz
            podstawa = ord('A') if znak.isupper() else ord('a')
            wynik += chr((ord(znak) - podstawa + przesuniecie) % 26 + podstawa)
        else:
            wynik += znak
    return wynik

print("Szyfr Cezara")
wiadomosc = input("Wprowadź tekst do zaszyfrowania: ")

while True:
    klucz_input = input("Podaj klucz (liczba całkowita): ").strip()
    if klucz_input.lstrip('-').isdigit():
        klucz = int(klucz_input)
        break
    else:
        print("Niepoprawny klucz! Wprowadź liczbę całkowitą.")

tryb = ""
while tryb not in ("szyfrowanie", "odszyfrowanie"):
    tryb = input("Wybierz tryb (szyfrowanie/odszyfrowanie): ").strip().lower()
    if tryb not in ("szyfrowanie", "odszyfrowanie"):
        print("Błąd! Wybierz szyfrowanie lub odszyfrowanie.")

wynik = szyfr_cezara(wiadomosc, klucz, tryb)
print(f"Wynik: {wynik}")