# Uppgift 4
# Skapa en funktion fibonacci(n) som returnerar en lista med de första n Fibonacci-talen.

def fibonacci(n: list) -> int:

   if n <= 0:
        return []  #Om n är 0 eller negativt. Returneras listan tom
   elif n == 1:
        return [0]  #Om  n är 1, returneras listan med det första fibonacci talet
    
   fib_sequence = [0, 1]  #Start värden
   while len(fib_sequence) < n: 
        next_value = fib_sequence[-1] + fib_sequence[-2] #Senaste två talen
        fib_sequence.append(next_value)  
   return fib_sequence
 
 
print (fibonacci(5))
print(fibonacci(0))
print(fibonacci(1))  
