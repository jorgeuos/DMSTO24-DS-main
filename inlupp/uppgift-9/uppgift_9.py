# Uppgift 9
# Skapa en funktion is_palindrome(string) som kontrollerar om en given sträng är ett palindrom (dvs. samma framifrån och bakifrån).

def is_palindrome(string):
    """
    Skriv beskrivning här.
    """
    return string == string[::-1]