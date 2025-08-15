from src.auxiliary_functions import (choice_1, choice_2, choice_3,
                                     selection_menu, try_get_data_from_file)
from src.exchange_api import ExchangeAPI
from src.interaction_with_API import HeadHunterAPI
from src.interaction_with_files import JSONSaver

if __name__ == "__main__":
    hh_api = HeadHunterAPI()
    rate_api = ExchangeAPI()
    rate_api.exchange_rate()
    json_saver = JSONSaver()

    while True:
        choice = selection_menu()

        if choice == 1:
            func_answer = choice_1(hh_api, json_saver)
            if func_answer == 1:
                continue

        elif choice == 2:
            data = try_get_data_from_file(json_saver)
            if not data:
                continue
            else:
                choice_2(data)

        elif choice == 3:
            data = try_get_data_from_file(json_saver)
            if not data:
                continue
            else:
                choice_3(data)

        elif choice == 4:
            break
