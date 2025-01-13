# Uppgift 10
# Skapa en funktion celsius_to_fahrenheit(celsius) som konverterar en temperatur från Celsius till Fahrenheit.

def celsius_to_fahrenheit(celsius: float) -> float:
    return celsius * 9/5 + 32  #multiplicera Celsius med 9/5 och sedan addera 32 för att få fahrenheit.

print(celsius_to_fahrenheit(0))    # Output: 32.0 (Frysning)
print(celsius_to_fahrenheit(100))  # Output: 212.0 (Kokning)
print(celsius_to_fahrenheit(-40))  # Output: -40.0 (Samma i båda skalorna)
