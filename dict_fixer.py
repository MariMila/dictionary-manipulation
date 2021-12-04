from dict_generator import response

def dict_fixer(users):
    states = {'Alagoas': 'Al', 'Sergipe': 'SE', 'Amapá': 'AP', 'Mato Grosso do Sul': 'MS', 'Paraíba': 'PB',
               'Amazonas': 'AM',
               'Roraima': 'RR', 'São Paulo': "SP", 'Bahia': "BH", 'Minas Gerais': "MG", 'Rio de Janeiro': "RJ"}
    python = {'The best language in the world': 'Python'}
    for student in users['users']:
        for index, course in enumerate(student['courses']):
            if course in python:
                student['courses'][index] = python[course]
        list_course = student['courses']
        student['state'] = states[student['state']]
        name = student['full name'].split()[0]
        surname = student['full name'].split()[1]
        student['email'] = student['email'].lower() if '@' in student['email'] else f'{name.lower()}.{surname.lower()}@gmail.com'
        student['zip_code'] = None if student['zip_code'] == 'unknown' else student['zip_code']
        student['address'] = None if 'unknown' in student['address'] else student['address']
        student['courses'] = {
            "number of courses": len(list_course),
            "hardworking student": len(list_course) > 2,
            "the best teacher's student": 'Python' in list_course,
            "student's course": list_course }
        print(student)
    return users

if __name__=='__main__':
    data = dict_fixer(response)
    print(data['users'])