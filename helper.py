import random

import allure
from faker import Faker

import courier_api
import data


class CourierFactory:
    @staticmethod
    def create_random_courier():
        fake = Faker()
        return {
            "login": fake.name(),
            "password": random.randint(1000, 9999),
            "firstName": fake.first_name()
        }

    @staticmethod
    def create_fake_courier():
        fake = Faker()
        return {
            "login": fake.name(),
            "password": random.randint(1000, 9999),
            }


class ChangeTestData:
    @staticmethod
    def modify_courier_body(key, value):
        body = data.TestData.COURIER_BODY.copy()
        body[key] = value
        return body


class CreateAndLogin:
    @staticmethod
    def create_courier_helper():
        create_courier_body = CourierFactory.create_random_courier()
        courier_body = {
            "login": create_courier_body['login'],
            "password": create_courier_body['password'],
        }
        courier_api.create_courier(create_courier_body)

        return courier_body

    @staticmethod
    def login_courier_and_get_id():
        courier_body = CreateAndLogin.create_courier_helper()
        return courier_api.login_courier(courier_body).json()['id']
