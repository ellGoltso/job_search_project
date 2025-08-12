from src.vacancy import Vacancy


def selection_menu() -> int:
    """Меню выбора опций пользователя"""
    while True:
        print(
            "Добро пожаловать! Выберите опцию:\n"
            "1. Ввести поисковый запрос для запроса вакансий из hh.ru\n"
            "2. Получить топ N вакансий по зарплате\n"
            "3. Получить вакансии с ключевым словом в описании.\n"
            "4. Выход из программы."
        )
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


def try_get_data_from_file(json_saver) -> list[dict]:
    """Функция пробует получить данные из json файла и вернуть список словарей с вакансиями,
    если файл не найден возвращает пустой список"""

    try:
        data = json_saver.get_data()
    except FileNotFoundError:
        print("Сначала выполните поиск вакансий.")
        return []
    return data


def choice_1(hh_api, json_saver) -> int:
    """В функции собрана последовательность вызова функций для поиска вакансий"""

    keyword = input("Введите запрос для поиска вакансий: ")
    hh_vacancies = hh_api.get_vacancies(keyword)
    if not hh_vacancies:
        print("Вакансий не найдено.")
        return 1
    vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)
    json_saver.add_data(vacancies_list)
    print("Вакансии сохранены в файл.")
    return 0


def choice_2(data):
    """В функции собрана последовательность вызова функций для вывода в консоль N-количества вакансий"""

    while True:
        try:
            top_n = int(
                input("Введите сколько вакансий вы хотите увидеть(введите число) ")
            )
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


def choice_3(data):
    """Функция предлагает пользователю ввести ключевое слово, сортирует вакансии по нему, и выводит в консоль"""

    vacancies_list = Vacancy.cast_to_obj_from_file(data)
    keyword = input("Введите ключевое слово: ")
    sorted_vacancies = []
    for vacancy in vacancies_list:
        if (
            vacancy.get_responsibility is not None
            and keyword in vacancy.get_responsibility
        ):
            sorted_vacancies.append(vacancy)

    print(sorted_vacancies)
