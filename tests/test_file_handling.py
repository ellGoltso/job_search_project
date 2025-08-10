from unittest.mock import mock_open, patch
import json
from src.interaction_with_files import JSONSaver
from src.vacancy import Vacancy


@patch("builtins.open", new_callable=mock_open)
def test_get_data(mock_file):
    data = [{"name": "Frontend-разработчик"}, {"name": "Преподаватель Frontend"}]
    mock_file.return_value.read.return_value = json.dumps(data)

    saver = JSONSaver("data/test_file_handling.json")
    saver.get_data()

    mock_file.assert_called_once_with(
        "data/test_file_handling.json", "r", encoding="utf-8"
    )


@patch("builtins.open", new_callable=mock_open)
def test_add_data(mock_file, vacancies_list):
    mock_file.return_value.read.return_value = json.dumps([])

    saver = JSONSaver("data/test_file_handling.json")
    saver.add_data(vacancies_list)

    mock_file.assert_any_call("data/test_file_handling.json", "r", encoding="utf-8")
    mock_file.assert_any_call("data/test_file_handling.json", "w", encoding="utf-8")


def test_delete_data(vacancies_after_del, vacancies_to_load):
    saver = JSONSaver("data/test.json")

    saver.add_data(vacancies_to_load)
    to_del = Vacancy(
        "Frontend-разработчик",
        39869,
        "RUB",
        "https://hh.ru/vacancy/123544177",
        "Минимум 2 года опыта в frontend web-<highlighttext>разработке</highlighttext>. "
        "Участие минимум в 5 реальных веб-проектах. Опыт работы с REST API. ",
        None,
    )

    saver.delete_data(to_del)
    assert saver.get_data() == vacancies_after_del
