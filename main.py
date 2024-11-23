from collections import Counter

czestotliwosci_liter = {
    'a': 0.085, 'b': 0.0207, 'c': 0.045388, 'd': 0.03385, 'e': 0.1116,
    'f': 0.01812, 'g': 0.0247, 'h': 0.03, 'i': 0.0755, 'j': 0.002,
    'k': 0.011, 'l': 0.0545, 'm': 0.0301, 'n': 0.06655, 'o': 0.071635,
    'p': 0.03167, 'q': 0.00196, 'r': 0.0758, 's': 0.05735, 't': 0.06951,
    'u': 0.03631, 'v': 0.01001, 'w': 0.0129, 'x': 0.0029, 'y': 0.01778,
    'z': 0.00272
}

def analiza_czestotliwosci(wiadomosc, liczba_wynikow=10):
    def oblicz_dopasowanie(tekst):
        licznik = Counter(znak.lower() for znak in tekst if znak.isalpha())
        suma_liter = sum(licznik.values())
        if suma_liter == 0:
            return 0
        dopasowanie = 0
        for znak, ilosc in licznik.items():
            czestotliwosc = ilosc / suma_liter
            oczekiwana_czestotliwosc = czestotliwosci_liter.get(znak, 0)
            dopasowanie += (czestotliwosc - oczekiwana_czestotliwosc) ** 2
        return -dopasowanie

    wyniki = []
    for klucz in range(26):
        odszyfrowana_wiadomosc = ''.join(
            chr((ord(znak) - ord('A') - klucz) % 26 + ord('A')) if znak.isupper() else
            chr((ord(znak) - ord('a') - klucz) % 26 + ord('a')) if znak.islower() else znak
            for znak in wiadomosc
        )
        dopasowanie = oblicz_dopasowanie(odszyfrowana_wiadomosc)
        wyniki.append((klucz, odszyfrowana_wiadomosc, dopasowanie))

    wyniki.sort(key=lambda x: x[2], reverse=True)
    return wyniki[:liczba_wynikow]

print("Analiza częstotliwości liter")

wiadomosc = input("Wprowadź zaszyfrowaną wiadomość: ")

while True:
    liczba_wynikow_input = input("Podaj liczbę najlepszych wyników do wyświetlenia (od 1 do 10): ").strip()
    if liczba_wynikow_input.isdigit() and 1 <= int(liczba_wynikow_input) <= 10:
        liczba_wynikow = int(liczba_wynikow_input)
        break
    else:
        print("Błąd! Podaj liczbę od 1 do 10.")

print("\nNajbardziej prawdopodobne odszyfrowania:")
wyniki = analiza_czestotliwosci(wiadomosc, liczba_wynikow)
for i, (klucz, tekst, dopasowanie) in enumerate(wyniki, 1):
    print(f"{i}. Klucz: {klucz}, Wiadomość: {tekst}")