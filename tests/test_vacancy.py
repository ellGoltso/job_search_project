from src.vacancy import Vacancy


def test_init_vacancy(vacancy_fixture):
    vacancy = Vacancy(
        "Директор по персоналу (HRD)",
        214222,
        "RUB",
        "https://hh.ru/vacancy/123856272",
        "Опыт в роли HR-директора / HRBP от 10 лет, преимущественно в технологических / "
        "производственных / международных стартапах. Опыт массового и точечного подбора...",
        "Уровень: Руководитель / HRD. Формирование и реализация HR-стратегии, "
        "соответствующей целям стартапа. Подбор ключевой команды: от инженерного до C‑level состава. ",
    )

    assert vacancy == vacancy_fixture
    assert (
        vacancy.get_responsibility
        == "Уровень: Руководитель / HRD. Формирование и реализация HR-стратегии, соответствующей целям стартапа. "
           "Подбор ключевой команды: от инженерного до C‑level состава. "
    )
    assert vacancy.name == "Директор по персоналу (HRD)"
    assert vacancy.currency == "RUB"
    assert vacancy.link_to_vacancy == "https://hh.ru/vacancy/123856272"
    assert (
        vacancy.requirement
        == "Опыт в роли HR-директора / HRBP от 10 лет, преимущественно в технологических / "
           "производственных / международных стартапах. Опыт массового и точечного подбора..."
    )


def test_cast_to_object(vacancies_list_dict, vacancies_list, hh_api_answer_fixture):
    vacancies = Vacancy.cast_to_object_list(hh_api_answer_fixture["items"])
    assert vacancies[0].name == "Заместитель директора по персоналу (HRD)"
    assert vacancies[0].salary == 50000
    assert vacancies[0].currency == "RUB"
    assert vacancies[0].link_to_vacancy == "https://hh.ru/vacancy/123848571"
    assert vacancies[0].requirement == (
        "Глубокие знания всех HR бизнес-процессов, "
        "успешный опыт их <highlighttext>разработки</highlighttext> и внедрения. "
        "Опыт написания стандартов, инструкций и регламентов "
    )
    assert vacancies[0].get_responsibility == (
        "Организация адаптации новых сотрудников. Построение и автоматизация HR процессов. "
        "Участие в <highlighttext>разработке</highlighttext> внутренних регламентов, должностных инструкций. "
        "Развитие HR-бренда, внешние..."
    )
    vacancies = Vacancy.cast_to_obj_from_file(vacancies_list_dict)
    assert vacancies == vacancies_list
