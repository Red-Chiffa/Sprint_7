import allure

import courier_api
import data
import helper


class TestLoginCourier:

    @allure.title('Проверка успешной авторизации курьера')
    def test_success_login_courier(self):
        response = courier_api.login_courier(data.TestData.COURIER_BODY)
        assert response.status_code == 200 and response.json()['id'] > 0 and response.json()['id'] is not None

    @allure.title('Проверка необходимости передачи обязательного поля - логин')
    def test_failed_login_courier_without_login(self):
        body = helper.ChangeTestData.modify_courier_body('login', '')
        created_courier_request = courier_api.login_courier(body)
        assert (created_courier_request.status_code == 400 and
                created_courier_request.json()['message'] == 'Недостаточно данных для входа')

    @allure.title('Проверка необходимости передачи обязательного поля - пароль')
    def test_failed_login_courier_without_password(self):
        body = helper.ChangeTestData.modify_courier_body('password', '')
        created_courier_request = courier_api.login_courier(body)
        assert (created_courier_request.status_code == 400 and
                created_courier_request.json()['message'] == 'Недостаточно данных для входа')

    @allure.title('Проверка ошибки при отправке запроса с несуществующей парой логин-пароль')
    def test_failed_login_courier_without_password(self):
        created_courier_request = courier_api.login_courier(helper.CourierFactory.create_fake_courier())
        assert (created_courier_request.status_code == 404 and
                created_courier_request.json()['message'] == 'Учетная запись не найдена')
