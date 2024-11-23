def szyfr_vigenere(wiadomosc, klucz, tryb="szyfrowanie"):
    wynik = ""
    klucz = klucz.lower()
    dlugosc_klucza = len(klucz)
    indeks_klucza = 0

    for znak in wiadomosc:
        if znak.isalpha():
            czy_duza = znak.isupper()
            przesuniecie = ord(klucz[indeks_klucza % dlugosc_klucza]) - ord('a')

            if tryb == "odszyfrowanie":
                przesuniecie = -przesuniecie

            podstawa = ord('A') if czy_duza else ord('a')
            wynik += chr((ord(znak) - podstawa + przesuniecie) % 26 + podstawa)

            indeks_klucza += 1
        else:
            wynik += znak

    return wynik

print("Szyfr Vigenère'a")

wiadomosc = input("Wprowadź tekst do zaszyfrowania lub odszyfrowania: ")

while True:
    klucz = input("Podaj klucz (ciąg liter): ").strip()
    if klucz.isalpha():
        break
    else:
        print("Błąd! Klucz musi składać się wyłącznie z liter.")

tryb = ""
while tryb not in ("szyfrowanie", "odszyfrowanie"):
    tryb = input("Wybierz tryb (szyfrowanie/odszyfrowanie): ").strip().lower()
    if tryb not in ("szyfrowanie", "odszyfrowanie"):
        print("Błąd! Wybierz szyfrowanie lub odszyfrowanie.")

wynik = szyfr_vigenere(wiadomosc, klucz, tryb)
print(f"Wynik: {wynik}")