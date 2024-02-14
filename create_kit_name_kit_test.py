import sender_stand_request
import data

#Функция, которая будет менять содержимое тела запроса
def get_kit_body(name):
    current_kit_body = data.kit_body.copy()
    current_kit_body["name"] = name
    return current_kit_body

# Функция для получения токена
def get_new_user_token():
    user_body = data.user_body
    resp_user = sender_stand_request.post_new_user(user_body)
    return resp_user.json()["authToken"]

# Функция для позитивных проверок (ОР - код 201)
def positive_assert(name):
    kit_body = get_kit_body(name)
    auth_token = get_new_user_token()
    user_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    assert user_response.status_code == 201
    assert user_response.json()["name"] == kit_body["name"]

# Тест 1. Успешное создание набора
# Параметр name состоит из 1 символа
def test_create_kit_1_letter_in_name_get_success_response():
    positive_assert("а")

# Тест 2. Успешное создание набора
# Параметр name состоит из 511 символов
def test_create_kit_511_letter_in_name_get_success_response():
    positive_assert("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda"
                    "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                    "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
                    "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"
                    "cdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda"
                    "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                    "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
                    "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")

# Тест 5. Успешное создание набора
# Параметр name состоит из английскиих букв
def test_create_kit_english_letter_in_name_get_success_response():
    positive_assert("QWErty")

# Тест 6. Успешное создание набора
# Параметр name состоит из русских букв
def test_create_kit_russian_letter_in_name_get_success_response():
    positive_assert("Мария")

# Тест 7. Успешное создание набора
# Параметр name состоит из спецсимволов
def test_create_kit_special_symbol_in_name_get_success_response():
    positive_assert("№'%,@")

# Тест 8. Успешное создание набора
# Параметр name состоит из слов с пробелами
def test_create_kit_has_space_in_name_get_success_response():
    positive_assert(" Человек и КО ")

# Тест 9. Успешное создание набора
# Параметр name состоит из цифр
def test_create_kit_has_number_in_name_get_success_response():
    positive_assert("123")

# Функции для негативных проверок (ОР - код 400)
# Функция для недопустимого количества символов
def negative_assert_symbol(name):
    kit_body = get_kit_body(name)
    auth_token = get_new_user_token()
    user_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    assert user_response.status_code == 400
    assert user_response.json()["code"] == 400

# Тест 4. Недопустимое создание набора
# Параметр name состоит из 512 символов
def test_create_kit_512_letter_in_name_get_error_response():
    negative_assert_symbol("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
                           "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                           "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda"
                           "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"
                           "cdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabc"
                           "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                           "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda"
                           "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"
                           "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")

# Функция для негативной проверки (пустое значение параметра и параметр не передан в запросе)
def negative_assert_no_name(kit_body):
    auth_token = get_new_user_token()
    response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    assert response.status_code == 400
    assert response.json()["code"] == 400

# Тест 3. Ошибка
# Параметр name состоит из пустой строки
def test_create_kit_empty_name_get_error_response():
    kit_body = get_kit_body("")
    negative_assert_no_name(kit_body)

# Тест 10. Ошибка
# В запросе нет параметра name
def test_create_kit_no_name_get_error_response():
    kit_body = data.kit_body.copy()
    kit_body.pop("name")
    negative_assert_no_name(kit_body)

# Тест 11. Ошибка
# Параметр name состоит из недопустимого типа данных - чисел
def test_create_kit_number_type_name_get_error_response():
    kit_body = get_kit_body(123)
    auth_token = get_new_user_token()
    response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    assert response.status_code == 400

