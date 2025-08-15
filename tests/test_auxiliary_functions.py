from src.auxiliary_functions import (choice_2, selection_menu,
                                     try_get_data_from_file)
from src.interaction_with_files import JSONSaver

# from src.vacancy import Vacancy
# import pytest


def test_try_get_data_from_incorrect_file():
    incorrect_saver = JSONSaver("data/incorrect_path.json")
    assert try_get_data_from_file(incorrect_saver) == []


def test_selection_menu(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "1")
    assert selection_menu() == 1


# def test_choice_2(monkeypatch, capsys, vacancies_list_dict):
#     monkeypatch.setattr('builtins.input', lambda _: "1")
#     choice_2(vacancies_list_dict)
#     expected_response = [{
#         "name": "Руководитель отдела продаж",
#         "salary": 198886,
#         "currency": "RUB",
#         "link_to_vacancy": "https://hh.ru/vacancy/123823544",
#         "requirement": "Инициативный, целеустремленный человек с гибким мышлением, "
#         "умеющий убеждать и находить точки. Соприкосновения с любым собеседником, "
#         "вызывать его интерес. ",
#         "responsibility": "1. Управление продажами: "
#         "<highlighttext>разработка</highlighttext> комплекса мероприятий, "
#         "позволяющих стабильно и долгосрочно достигать. "
#         "Запланированных показателей выручки и прибыли. "
#         "2. Определение стратегии и...",
#     }]
#     expected_response = Vacancy.cast_to_obj_from_file(expected_response)
#     assert capsys.readouterr() == f"{expected_response.__repr__()}\n"
#
