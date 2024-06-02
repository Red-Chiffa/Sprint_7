import requests
import urls


def create_courier(body):
    return requests.post(urls.CREATE_COURIER_URL, json=body)


def login_courier(body):
    return requests.post(urls.LOGIN_COURIER_URL, json=body)


def get_id_courier(body):
    return requests.post(urls.LOGIN_COURIER_URL, json=body).json()['id']


def delete_courier(url):
    return requests.delete(url)


def create_order(body):
    return requests.post(urls.ORDER, json=body)


def get_order_list():
    return requests.get(urls.ORDER)


def get_couriers_order_list(id):
    return requests.get(urls.ORDER, headers={'courierId': id})

