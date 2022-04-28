# Task 2

# Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Осуществить вывод данных о пользователе одной строкой.


def data_print(name, surname, birth_year, city, email, phone):
    print(f'Имя: {name}, Фамилия: {surname}, Год рождения: {birth_year}, Город проживания: {city}, Электронный адрес: '
          f'{email}, Телефон: {phone}')


inp_name = input('Введите имя: ')
inp_surname = input('Введите фамилию: ')
inp_birth_year = input('Введите год рождения: ')
inp_city = input('Введите город проживания: ')
inp_email = input('Введите электронный адрес: ')
inp_phone = input('Введите телефон: ')

data_print(name=inp_name, surname=inp_surname, birth_year=inp_birth_year, city=inp_city, email=inp_email,
           phone=inp_phone)
