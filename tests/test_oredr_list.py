import allure
from unittest.mock import patch
import courier_api


class TestOrderList:

    @allure.title('Проверка получения списка всех заказов')
    def test_success_get_order_list(self):
        response = courier_api.get_order_list()
        assert response.status_code == 200 and response.json()['orders'] is not None
