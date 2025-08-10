from unittest.mock import Mock, patch

from src.interaction_with_API import HeadHunterAPI, ExchangeAPI


@patch("requests.get")
def test_hh_api(mock_get, hh_api_answer_fixture):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = hh_api_answer_fixture
    mock_get.return_value = mock_response

    hh_api = HeadHunterAPI()
    vacancies = hh_api.get_vacancies("test")

    assert vacancies[0]["name"] == "Заместитель директора по персоналу (HRD)"


@patch("requests.request")
def test_exchange_api(mock_get, exchange_api_answer_fixture):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = exchange_api_answer_fixture
    mock_get.return_value = mock_response

    exchange_api = ExchangeAPI()
    exchange_api.exchange_rate("data/test_exchange_rate.json")

    mock_get.assert_called_once()
