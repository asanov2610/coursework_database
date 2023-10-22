from api import Api_work
from api import Data_file
from database import DBManager


print('Поехали!')


api_result = Api_work()
vacant = api_result.get_api_vacancies()
vac_dict = api_result.vacancy_data(vacant)
emp_dict = api_result.employer_data(vacant)

print("Найдены вакансии с hh.ru")

Data_file.vacancy_file_create(vac_dict)
Data_file.employer_file_create(emp_dict)
db_result = DBManager()
db_result.create_db_of_vacancies()
db_result = DBManager()
db_result.create_db_of_employers()
db_result = DBManager()
db_result.filling_db_of_vacancies()
db_result = DBManager()
db_result.filling_db_of_employer()
print('Вакансии записаны в таблицы базы данных: "coursework_5"')
print('Попробуем сформировать запросы?')
print('\n')
while True:
    print('Выбери из списка:\n'
            "1 - Вывод списка всех компаний и кол-ва вакансий у каждой из них; \n"
            "2 - Вывод списка всех вакансий; \n"
            "3 - Вывести среднюю зарплату по вакансиям; \n"
            "4 - Вывод списка всех вакансий, у которых зарплата выше средней по всем вакансиям; \n"
            "5 - Вывод списка всех вакансий в названии которых будем искать твой запрос; \n"
            "'quit' - для выхода. \n"
    )
    choose = input()

    if choose.lower() == "quit":
        Data_file.vacancy_file_clear()
        Data_file.employer_file_clear()
        db_result = DBManager()
        db_result.delete_db_of_vacancies()
        db_result = DBManager()
        db_result.delete_db_of_epmloyer()
        break
    elif choose == '1':
        db_result = DBManager()
        data = db_result.get_companies_and_vacancies_count()

    elif choose == '2':
        db_result = DBManager()
        data = db_result.get_all_vacancies()

    elif choose == '3':
        db_result = DBManager()
        data = db_result.get_avg_salary()

    elif choose == '4':
        db_result = DBManager()
        data = db_result.get_vacancies_with_higher_salary()

    elif choose == '5':
        print('Ведите ключевое слово для запроса')
        keyword = input().capitalize()
        db_result = DBManager()
        data = db_result.get_vacancies_with_keyword(keyword)

    else:
        print('Нет такого варианта')
        continue