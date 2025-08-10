import json

from src.interaction_with_API import HeadHunterAPI, ExchangeAPI
from src.vacancy import Vacancy
from src.interaction_with_files import JSONSaver


def selection_menu() -> int:
    while True:
        print("Добро пожаловать! Выберите опцию:\n"
              "1. Ввести поисковый запрос для запроса вакансий из hh.ru\n"
              "2. Получить топ N вакансий по зарплате\n"
              "3. Получить вакансии с ключевым словом в описании.\n"
              "4. Выход из программы.")
        choice_str = input("Введите номер опции: ").strip()
        try:
            choice_int = int(choice_str)
        except ValueError:
            print("Введите число")
            continue
        else:
            if choice_int < 1 or choice_int > 4:
                print("Введите число от 1 до 4")
                continue
            return choice_int


if __name__ == "__main__":
    hh_api = HeadHunterAPI()
    rate_api = ExchangeAPI()
    rate_api.exchange_rate()
    json_saver = JSONSaver()

    while True:
        choice = selection_menu()

        if choice == 1:
            keyword = input("Введите запрос для поиска вакансий: ")
            hh_vacancies = hh_api.get_vacancies(keyword)
            if not hh_vacancies:
                print("Вакансий не найдено.")
                continue
            vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)
            json_saver.add_data(vacancies_list)
            print(json.dumps(json_saver.get_data(), indent=4, ensure_ascii=False))

        elif choice == 2:
            try:
                data = json_saver.get_data()
            except FileNotFoundError:
                print("Сначала выполните поиск вакансий.")
                continue

            while True:
                try:
                    top_n = int(input("Введите сколько вакансий вы хотите увидеть(введите число) "))
                except ValueError:
                    print("Введите число")
                    continue
                if top_n > len(data):
                    print("В подборке нет столько вакансий.")
                    continue
                elif top_n < 1:
                    print("Введите число больше 0.")
                    continue
                vacancies_list = Vacancy.cast_to_obj_from_file(data)
                vacancies_list.sort(reverse=True)
                print(vacancies_list[:top_n])
                break

        elif choice == 3:
            try:
                data = json_saver.get_data()
            except FileNotFoundError:
                print("Сначала выполните поиск вакансий.")
                continue

            vacancies_list = Vacancy.cast_to_obj_from_file(data)
            keyword = input("Введите ключевое слово: ")
            sorted_vacancies = []
            for vacancy in vacancies_list:
                if vacancy.get_responsibility is not None and keyword in vacancy.get_responsibility:
                    sorted_vacancies.append(vacancy)

            print(sorted_vacancies)

        elif choice == 4:
            break


# # Пример работы контструктора класса с одной вакансией
# vacancy = Vacancy("Python Developer", "<https://hh.ru/vacancy/123456>", "100 000", "Требования: опыт работы от 3 лет...")

# json_saver.delete_vacancy(vacancy)
#
# # Функция для взаимодействия с пользователем
# def user_interaction():
#     platforms = ["HeadHunter"]
#     search_query = input("Введите поисковый запрос: ")
#     top_n = int(input("Введите количество вакансий для вывода в топ N: "))
#     filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
#     salary_range = input("Введите диапазон зарплат: ") # Пример: 100000 - 150000
#
#     filtered_vacancies = filter_vacancies(vacancies_list, filter_words)
#
#     ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)
#
#     sorted_vacancies = sort_vacancies(ranged_vacancies)
#     top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
#     print_vacancies(top_vacancies)
#
#
# if __name__ == "__main__":
#     user_interaction()