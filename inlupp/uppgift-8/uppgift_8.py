# Uppgift 8
# Skapa en funktion count_letters(string) som returnerar en dictionary med varje bokstav som nyckel och antalet förekomster som värde.

def count_letters(string: str) -> dict:
    letter_counts = {}  #Skapa en tom dictionary för att lagra resultaten
    for char in string:  #Gå igenom varje tecken i strängen
        if char.isalpha():  #Kontrollera om tecknet är en bokstav
            char = char.lower()  #Gör tecknet till gemen för att ignorera skillnad mellan stora/små bokstäver
            if char in letter_counts:  #Om bokstaven redan finns i dictionaryn
                letter_counts[char] += 1  #Öka räknaren med 1
            else:  #Om bokstaven inte finns i dictionaryn
                letter_counts[char] = 1  #Lägg till bokstaven med värdet 1
    return letter_counts  #Returnera den färdiga dictionaryn   
 

    print(count_letters("Hej Sverige!"))
