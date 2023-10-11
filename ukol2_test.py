# Firma eviduje informace o počtu součástek na skladě ve slovníku. 
# Klíč slovníku je kód součástky, hodnota klíče je počet součástek na skladě.

sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}

soucastka = input("Uveďte kód požadované součástky: ")
mnozstvi = int(input("Uveďte požadované množství: "))

if soucastka not in sklad:  
    print("Součástka není skladem.")
else:
    pocet_skladem = 0
    for kod, kusy in sklad.items():
        pocet_skladem += kusy
        if kod in sklad and mnozstvi > kusy:  
            print("Lze prodat pouze omezené množství kusů.")
            # sklad.pop[kod]
        if kod in sklad and mnozstvi < kusy:                  
            print("Skladem je dostatečné množství kusů.")
            soucastky_novy_pocet = sklad[kod] - mnozstvi           
            print(f"Skladem zbývá {soucastky_novy_pocet} kusů.")
