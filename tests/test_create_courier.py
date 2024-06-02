import allure
import courier_api
import helper


class TestCreateCourier:

    @allure.title('Проверка успешного создания курьера и того, что успешный запрос возвращает {"ok":true}')
    def test_success_create_courier(self):
        created_courier_request = courier_api.create_courier(helper.CourierFactory.create_random_courier())
        assert created_courier_request.status_code == 201 and created_courier_request.json()["ok"] == True

    @allure.title('Проверка ошибки при создании двух одинаковых курьеров')
    def test_failed_create_duplicate_courier(self):
        body = helper.CourierFactory.create_random_courier()
        courier_api.create_courier(body)
        created_courier_request = courier_api.create_courier(body)
        assert (created_courier_request.status_code == 409 and
                "Этот логин уже используется" in created_courier_request.json()['message'])

    @allure.title('Проверка необходимости передачи обязательного поля - логин')
    def test_failed_create_courier_without_login(self):
        body = helper.ChangeTestData.modify_courier_body('login', '')
        created_courier_request = courier_api.create_courier(body)
        assert (created_courier_request.status_code == 400 and
                created_courier_request.json()['message'] == 'Недостаточно данных для создания учетной записи')

    @allure.title('Проверка необходимости передачи обязательного поля - пароль')
    def test_failed_create_courier_without_password(self):
        body = helper.ChangeTestData.modify_courier_body('password', '')
        created_courier_request = courier_api.create_courier(body)
        assert (created_courier_request.status_code == 400 and
                created_courier_request.json()['message'] == 'Недостаточно данных для создания учетной записи')
