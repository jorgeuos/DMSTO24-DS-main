# Uppgift 11
# Skapa en funktion word_count(text) som returnerar antalet ord i en given text.

def word_count(text: str) -> int:
    words = text.split()  # Dela texten i en lista av ord
    return len(words)     # Returnera längden på listan

print(word_count("Hej, hur mår du?"))         # Output: 4
print(word_count("Stockholm city"))          # Output: 5
print(word_count(""))                          # Output: 0
