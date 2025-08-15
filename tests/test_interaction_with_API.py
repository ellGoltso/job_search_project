from unittest.mock import Mock, patch

from src.interaction_with_API import HeadHunterAPI


@patch("requests.get")
def test_hh_api(mock_get, hh_api_answer_fixture):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = hh_api_answer_fixture
    mock_get.return_value = mock_response

    hh_api = HeadHunterAPI()
    vacancies = hh_api.get_vacancies("test")

    assert vacancies[0]["name"] == "Заместитель директора по персоналу (HRD)"
