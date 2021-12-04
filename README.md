# Dictionary Manipulation

## Description

I, Mariana Romão, am a Python instructor, to encourage my students to master the manipulation of dictionaries I challenged them to code the following challenge:

> Make code that reads the dictionary and makes the following changes
>
> 1 - The names of the states must be replaced by their respective acronyms.
>
> 2 - Whenever there is an unknown data, switch to the null variable
>
> 3 - email: if it's unknown, switch it to the template "firstname.surname@gmail.com", ensure that ALL EMAILS are in lower case
>
> 4 - Switch all "The best language in the world" to "Python"
>
> 5 - Switch the value of the "course" key to the following output:

> 'courses' = {
>
>            "number of courses": int,
>
>            "hardworking student": True | False,
>
>            "the best teacher's student": True | False,
>
>            "student's course": student's list of course}

> The student will be a hardworking one if they takes more than 2 courses
>
> The student will be a best teacher's student one if there is Python in their list of courses

### Input
```
{'full name': 'Joao Silva', 
'state': 'Roraima', 
'email': 'unknown', 
'courses': ['Assembly', 'Rusty', 'JavaScript', 'C++'], 
'phone': 9964382936, 
'address': 'Travessa Girassol', 
'zip_code': 'unknown'}
```

### Output
```
{'full name': 'Joao Silva', 
'state': 'RR', 
'email': 'joao.silva@gmail.com', 
'courses': {
    'number of courses': 4, 
    'hardworking student': True, 
    "the best teacher's student": False, 
    "student's course": ['Assembly', 'Rusty', 'JavaScript', 'C++']
    }, 
'phone': 9964382936, 
'address': 'Travessa Girassol', 
'zip_code': None}
```



## Resolution

> dict_generator.py generates a dict to be handled
>
> run the dict_fixer.py to see all inputs treatment 