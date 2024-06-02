import allure
import pytest

import courier_api


class TestCreateOrder:

    @allure.description('параметризованный тест проверяет оформление заказа с разным цветом самоката')
    @allure.title('оформление заказа')
    @pytest.mark.parametrize('colour', [['BLACK'], ['GREY'], ['BLACK', 'GREY'], ['']])
    def test_success_create_order(self, colour):
        body = {
            "firstName": "Naruto",
            "lastName": "Uchiha",
            "address": "Konoha, 142 apt.",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2020-06-06",
            "comment": "Saske, come back to Konoha",
            "color": colour
        }
        created_order = courier_api.create_order(body)
        assert (created_order.status_code == 201 and
                created_order.json()['track'] > 0 and created_order.json()['track'] is not None)
