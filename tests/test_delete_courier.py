import allure

import courier_api
import helper
import urls


class TestDeleteCourier:

    @allure.title('Проверка успешного удаления курьера')
    def test_succes_delete_courier(self):
        id = courier_api.login_courier(helper.CreateAndLogin.create_courier_helper()).json()['id']
        delete_response = courier_api.delete_courier(urls.DELETE_COURIER_URL + f"/{id}")
        assert delete_response.status_code == 200 and delete_response.json()['ok'] == True

    @allure.title('Проверка появления ошибки при удалении курьера без id')
    @allure.description('Тест падает, т.к. приходит неверный код ответа')  # Проверила в Postman - 404 "Not Found."
    def test_failed_delete_courier_without_id(self):
        delete_response = courier_api.delete_courier(urls.DELETE_COURIER_URL)
        assert (delete_response.status_code == 400 and
                delete_response.json()['message'] == "Недостаточно данных для удаления курьера")

    @allure.title('Проверка появления ошибки при удалении курьера с неверным id')
    def test_failed_delete_courier_with_wrong_id(self):
        delete_response = courier_api.delete_courier(urls.DELETE_COURIER_URL + '/-1')
        assert (delete_response.status_code == 404 and
                delete_response.json()['message'] == "Курьера с таким id нет.")
