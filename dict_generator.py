"""
This code will generate the dictionary that will be handled by the dict_fixer module.
"""

from random import randrange, choice


users = []


def dict_generator():
    for i in range(90):
        states_list = "São Paulo, Sergipe, Bahia, Rio de Janeiro, Mato Grosso do Sul, Alagoas, Amapá, Amazonas, Roraima, Minas Gerais, Paraíba"
        states_list = states_list.split(', ')
        names = "Joao, Maria, Jose, Heleonor, Heloisa, Katia, Regina, Suellen, Eduardo, Pedro, Henrique, Matheus, Gabriel, Vinicius"
        surnames = "Teixeira, Esteque, Estevan, Falabella, Torres, Romano, Neves, Silva, Barroso"
        names = names.split(', ')
        surnames = surnames.split(', ')
        courses = "The best language in the world, JavaScript, Java, C#, C++, Go, Ruby, Rusty, Assembly, Pascal"
        courses = courses.split(", ")
        logradouro = "Avenida, street, Travessa, Estrada, Viela"
        name_street = "Flores, Alemanhã, Joana d'Arc, Girassol, Túlipa, França"
        logradouro = logradouro.split(", ")
        name_street = name_street.split(", ")
        name = choice(names)
        surname = choice(surnames)
        num_courses = randrange(len(courses))
        course_u = []
        email = [f"{name}.{surname}@gmail.com", f"{name}.{surname}@gmail.com", f"{name}.{surname}@gmail.com", 'unknown']
        address = [f'{choice(logradouro)} {choice(name_street)}', f'{choice(logradouro)} {choice(name_street)}', f'{choice(logradouro)} {choice(name_street)}', f'{choice(logradouro)} {choice(name_street)}', 'unknown']
        zip_code = [randrange(1000000, 9999999), randrange(1000000, 9999999), randrange(1000000, 9999999), 'unknown']
        for cur in range(num_courses):
            cursin = choice(courses)
            if cursin not in course_u:
                course_u.append(cursin)
        user = {
            'full name': name + ' ' + surname,
            'state': choice(states_list),
            'email': choice(email),
            'courses': course_u,
            'phone': randrange(9000000000, 10000000000),
            'address': choice(address),
            'zip_code': choice(zip_code)
        }
        users.append(user)


dict_generator()


response = {'users': users}
print(response)