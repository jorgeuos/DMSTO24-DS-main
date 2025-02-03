# Uppgift 7
# Skapa en funktion validate_password(password) som kontrollerar att lösenordet är minst 8 tecken långt och innehåller minst en siffra.

def validate_password(password):
    """
    Skriv beskrivning här.
    """
    return len(password) >= 8 and any(char.isdigit() for char in password)