# Uppgift 3
# Hitta det största talet i en lista

def max_in_list(numbers: list) -> int:
   
    highest = numbers[0]  #Sätt första värdet som högst initialt
    for num in numbers:
        if num > highest:  #om ett större värde hittas
            highest = num  #Uppdatera högsta värdet
    return highest #Retunera det största värdet 
 
 
print(max_in_list([1, 2, 3])) 
print(max_in_list([-5, 0, 5]))
print(max_in_list([10]))
