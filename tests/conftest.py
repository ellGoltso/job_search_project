from src.vacancy import Vacancy
import pytest


@pytest.fixture
def vacancy_fixture():
    vacancy_dict = {
        "name": "Директор по персоналу (HRD)",
        "salary": 214222,
        "currency": "RUB",
        "link_to_vacancy": "https://hh.ru/vacancy/123856272",
        "requirement": "Опыт в роли HR-директора / HRBP от 10 лет, преимущественно "
                       "в технологических / производственных "
                       "/ международных стартапах. Опыт массового и точечного подбора...",
        "responsibility": "Уровень: Руководитель / HRD. "
                          "Формирование и реализация HR-стратегии, "
                          "соответствующей целям стартапа. Подбор ключевой команды: "
                          "от инженерного до C‑level состава. ",
    }
    return Vacancy(**vacancy_dict)


@pytest.fixture
def vacancies_list_dict():
    vacancy_dict_1 = {
        "name": "Руководитель отдела продаж",
        "salary": 198886,
        "currency": "RUB",
        "link_to_vacancy": "https://hh.ru/vacancy/123823544",
        "requirement": "Инициативный, целеустремленный человек с гибким мышлением, "
                       "умеющий убеждать и находить точки. Соприкосновения с любым собеседником, "
                       "вызывать его интерес. ",
        "responsibility": "1. Управление продажами: "
                          "<highlighttext>разработка</highlighttext> комплекса мероприятий, "
                          "позволяющих стабильно и долгосрочно достигать. "
                          "Запланированных показателей выручки и прибыли. "
                          "2. Определение стратегии и...",
    }
    vacancy_dict_2 = {
        "name": "Frontend-разработчик",
        "salary": 39869,
        "currency": "RUB",
        "link_to_vacancy": "https://hh.ru/vacancy/123544177",
        "requirement": "Минимум 2 года опыта в frontend web-<highlighttext>разработке</highlighttext>."
                       " Участие минимум в 5 реальных веб-проектах. Опыт работы с REST API. ",
        "responsibility": None,
    }
    vacancy_dict_3 = {
        "name": "Junior Frontend разработчик",
        "salary": 100000,
        "currency": "RUB",
        "link_to_vacancy": "https://hh.ru/vacancy/123648356",
        "requirement": "Знание Git. Знание JS/HTML/CSS. Знание Vue.js, React, vite. Умение писать SQL.",
        "responsibility": None,
    }
    return [vacancy_dict_1, vacancy_dict_2, vacancy_dict_3]


@pytest.fixture
def vacancies_list():
    vacancy_1 = Vacancy(
        "Руководитель отдела продаж",
        198886,
        "RUB",
        "https://hh.ru/vacancy/123823544",
        "Инициативный, целеустремленный человек с гибким мышлением,"
        " умеющий убеждать и находить точки. Соприкосновения с любым собеседником, вызывать его интерес. ",
        "1. Управление продажами: <highlighttext>разработка</highlighttext> комплекса мероприятий, "
        "позволяющих стабильно и долгосрочно достигать. Запланированных показателей выручки и прибыли. "
        "2. Определение стратегии и...",
    )
    vacancy_2 = Vacancy(
        "Frontend-разработчик",
        39869,
        "RUB",
        "https://hh.ru/vacancy/123544177",
        "Минимум 2 года опыта в frontend web-<highlighttext>разработке</highlighttext>. "
        "Участие минимум в 5 реальных веб-проектах. Опыт работы с REST API. ",
        None,
    )

    vacancy_3 = Vacancy(
        "Junior Frontend разработчик",
        100000,
        "RUB",
        "https://hh.ru/vacancy/123648356",
        "Знание Git. Знание JS/HTML/CSS. Знание Vue.js, React, vite. Умение писать SQL.",
        None,
    )

    return [vacancy_1, vacancy_2, vacancy_3]


@pytest.fixture
def vacancies_after_del():
    return [
        {
            "name": "Junior Frontend разработчик",
            "salary": 0,
            "currency": "",
            "link_to_vacancy": "https://hh.ru/vacancy/123648356",
            "requirement": "Знание Git. Знание JS/HTML/CSS. Знание Vue.js, React, vite. "
                           "Умение писать SQL. Умение подключать API, асинхронная подгрузка, кеширование. ",
            "responsibility": None,
        },
        {
            "name": "Преподаватель Frontend",
            "salary": 76074,
            "currency": "RUB",
            "link_to_vacancy": "https://hh.ru/vacancy/123841236",
            "requirement": "Опыт работы в сфере Frontend-<highlighttext>разработки</highlighttext> "
                           "или преподавания от 1 года. Уверенное знание HTML, CSS, JavaScript и "
                           "одного или нескольких...",
            "responsibility": "Знание узбекского и русского языков. "
                              "<highlighttext>Разработка</highlighttext> и актуализация учебных материалов. "
                              "Консультирование учеников и проверка практических заданий. "
                              "Участие в <highlighttext>разработке</highlighttext> и...",
        },
    ]


@pytest.fixture
def vacancies_to_load():
    return [
        Vacancy(
            "Junior Frontend разработчик",
            0,
            "",
            "https://hh.ru/vacancy/123648356",
            "Знание Git. Знание JS/HTML/CSS. Знание Vue.js, React, vite. "
            "Умение писать SQL. Умение подключать API, асинхронная подгрузка, кеширование. ",
            None,
        ),
        Vacancy(
            "Frontend-разработчик",
            39869,
            "RUB",
            "https://hh.ru/vacancy/123544177",
            "Минимум 2 года опыта в frontend web-<highlighttext>разработке</highlighttext>. "
            "Участие минимум в 5 реальных веб-проектах. Опыт работы с REST API. ",
            None,
        ),
        Vacancy(
            "Преподаватель Frontend",
            76074,
            "RUB",
            "https://hh.ru/vacancy/123841236",
            "Опыт работы в сфере Frontend-<highlighttext>разработки</highlighttext> "
            "или преподавания от 1 года. Уверенное знание HTML, CSS, JavaScript и одного или нескольких...",
            "Знание узбекского и русского языков. <highlighttext>Разработка</highlighttext> "
            "и актуализация учебных материалов. Консультирование учеников и проверка практических заданий. "
            "Участие в <highlighttext>разработке</highlighttext> и...",
        ),
    ]


@pytest.fixture
def exchange_api_answer_fixture():
    return {
        "success": True,
        "timestamp": 1754823556,
        "source": "RUB",
        "quotes": {
            "RUBGBP": 0.009338,
            "RUBJPY": 1.851558,
            "RUBEUR": 0.010766,
            "RUBUZS": 157.739505,
            "RUBUSD": 0.012541,
            "RUBAZN": 0.021369,
            "RUBKZT": 6.768676,
            "RUBKGS": 1.096707,
            "RUBBYN": 0.041353,
        },
    }


@pytest.fixture
def hh_api_answer_fixture():
    return {
        "items": [
            {
                "id": "123848571",
                "premium": False,
                "name": "Заместитель директора по персоналу (HRD)",
                "department": None,
                "has_test": False,
                "response_letter_required": False,
                "area": {
                    "id": "1002",
                    "name": "Минск",
                    "url": "https://api.hh.ru/areas/1002",
                },
                "salary": {
                    "from": 45000,
                    "to": 55000,
                    "currency": "RUR",
                    "gross": False,
                },
                "salary_range": {
                    "from": 45000,
                    "to": 55000,
                    "currency": "RUR",
                    "gross": False,
                    "mode": {"id": "MONTH", "name": "За\xa0месяц"},
                    "frequency": {
                        "id": "TWICE_PER_MONTH",
                        "name": "Два раза в\xa0месяц",
                    },
                },
                "type": {"id": "open", "name": "Открытая"},
                "address": {
                    "city": "деревня Тарасово",
                    "street": "Тарасовский проезд",
                    "building": "3",
                    "lat": 53.922268,
                    "lng": 27.394044,
                    "description": None,
                    "raw": "деревня Тарасово, Тарасовский проезд, 3",
                    "metro": {
                        "station_name": "Каменная Горка",
                        "line_name": "Автозаводская",
                        "station_id": "63.416",
                        "line_id": "63",
                        "lat": 53.90683,
                        "lng": 27.437558,
                    },
                    "metro_stations": [
                        {
                            "station_name": "Каменная Горка",
                            "line_name": "Автозаводская",
                            "station_id": "63.416",
                            "line_id": "63",
                            "lat": 53.90683,
                            "lng": 27.437558,
                        }
                    ],
                    "id": "17046599",
                },
                "response_url": None,
                "sort_point_distance": None,
                "published_at": "2025-08-08T17:54:14+0300",
                "created_at": "2025-08-08T17:54:14+0300",
                "archived": False,
                "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=123848571",
                "show_contacts": False,
                "insider_interview": None,
                "url": "https://api.hh.ru/vacancies/123848571?host=hh.ru",
                "alternate_url": "https://hh.ru/vacancy/123848571",
                "relations": [],
                "employer": {
                    "id": "11395690",
                    "name": "ГлобалГринДеко",
                    "url": "https://api.hh.ru/employers/11395690",
                    "alternate_url": "https://hh.ru/employer/11395690",
                    "logo_urls": None,
                    "vacancies_url": "https://api.hh.ru/vacancies?employer_id=11395690",
                    "accredited_it_employer": False,
                    "trusted": True,
                },
                "snippet": {
                    "requirement": "Глубокие знания всех HR бизнес-процессов, успешный опыт их "
                                   "<highlighttext>разработки</highlighttext> и внедрения. "
                                   "Опыт написания стандартов, инструкций и регламентов ",
                    "responsibility": "Организация адаптации новых сотрудников. "
                                      "Построение и автоматизация HR процессов. "
                                      "Участие в <highlighttext>разработке</highlighttext> внутренних регламентов, "
                                      "должностных инструкций. Развитие HR-бренда, внешние...",
                },
                "contacts": None,
                "schedule": {"id": "fullDay", "name": "Полный день"},
                "working_days": [],
                "working_time_intervals": [],
                "working_time_modes": [],
                "accept_temporary": False,
                "fly_in_fly_out_duration": [],
                "work_format": [{"id": "ON_SITE", "name": "На\xa0месте работодателя"}],
                "working_hours": [{"id": "HOURS_8", "name": "8\xa0часов"}],
                "work_schedule_by_days": [{"id": "FIVE_ON_TWO_OFF", "name": "5/2"}],
                "night_shifts": False,
                "professional_roles": [
                    {"id": "38", "name": "Директор по персоналу (HRD)"}
                ],
                "accept_incomplete_resumes": False,
                "experience": {"id": "between3And6", "name": "От 3 до 6 лет"},
                "employment": {"id": "full", "name": "Полная занятость"},
                "employment_form": {"id": "FULL", "name": "Полная"},
                "internship": False,
                "adv_response_url": None,
                "is_adv_vacancy": False,
                "adv_context": None,
            }
        ]
    }
