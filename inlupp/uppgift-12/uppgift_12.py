# Uppgift 12
# Skapa en funktion create_student_register(students) som tar emot en lista med namn och ålder och returnerar en dictionary där namnet är nyckeln och åldern är värdet.

def create_student_register(students: list) -> dict:
    return {name: age for name, age in students}

students = [("Anna", 20), ("Erik", 22), ("Lisa", 19)]
register = create_student_register(students)
print(register)
