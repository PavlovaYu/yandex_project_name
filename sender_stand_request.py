import configuration
import requests
import data

# Запрос на создание нового пользователя
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)

# Функция создания нового набора
def post_new_client_kit(kit_body, auth_token):
    current_auth_token = data.headers.copy()
    current_auth_token["Authorization"] = "Bearer " + str(auth_token)
    return requests.post(configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH, json=kit_body,
                         headers=current_auth_token)


