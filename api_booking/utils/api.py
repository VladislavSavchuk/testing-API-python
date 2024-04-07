"""Методы для получения, добавления, изменения и удаления книги"""

# импортируем класс Http_methods из файла http_methods.py папки utils
from utils.http_methods import Http_methods

# базовая URL для всех запросов
base_url = 'https://restful-booker.herokuapp.com'

# Добавляем декоратор @staticmethod. Делаем методы статическими (без self). Созданный метод не привязывается
# к классу Booking, и может вызываться в любом другом классе или тесте


class Booking:
    """Метод для создания токена"""
    # Creates a new auth token to use for access to the PUT and DELETE /booking
    # https://restful-booker.herokuapp.com/apidoc/index.html
    @staticmethod
    def create_new_token():
        # ресурс метода POST
        post_token = '/auth'

        # создаем полный url запроса
        token_url = base_url + post_token
        print(token_url)

        # имя и пароль пользователя для аутентификации к сайту в json-формате
        json_for_auth = {
            "username": "admin",
            "password": "password123"
        }

        # Получаем результат. Обращаемся к классу "Http_methods" и выбираем необходимый запрос "post".
        # Указываем "url" запроса и передаем данные аутентификации в json-формате
        result_token = Http_methods.post(token_url, json_for_auth)

        # указываем кодировку ответа и выводим результат ответа в текстовом формате
        result_token.encoding = 'utf-8'
        print(result_token.text)

        # возвращаем result_token для использования результата в методе "test_create_new_book" файла test_booking.py
        return result_token

    """Метод для создания новой книги"""
    @staticmethod
    def create_new_book():
        # ресурс метода POST
        post_resource = '/booking'

        # создаем полный url запроса метода POST
        post_url = base_url + post_resource
        print(post_url)

        # создаем информацию о новой книге в json-формате
        json_for_create_new_book = {
            "firstname": "James",
            "lastname": "Smith",
            "totalprice": 999,
            "depositpaid": False,
            "bookingdates": {
                "checkin": "2023-01-01",
                "checkout": "2024-01-01"
            },
            "additionalneeds": "QA"
        }

        # Получаем результат. Обращаемся к классу "Http_methods" и выбираем необходимый метод "post".
        # Указываем "url" запроса и информацию в json-формате, т.к. для метода POST нужно тело запроса
        result_post = Http_methods.post(post_url, json_for_create_new_book)

        # указываем кодировку ответа и выводим результат ответа в текстовом формате
        result_post.encoding = 'utf-8'
        print(result_post.text)

        # возвращаем result_post для использования результата в методе "test_create_new_book" файла test_booking.py
        return result_post

    """Метод для проверки создания новой книги"""
    @staticmethod
    # Находим booking_id книги и передаем в метод get_new_book.
    # booking_id определяем в методе test_create_new_book класса Test_new_book в файле test_booking.py
    def get_new_book(booking_id):
        # ресурс метода GET
        get_resource = '/booking/'

        # создаем полный url запроса метода GET
        get_url = base_url + get_resource + str(booking_id)
        print(get_url)

        # Получаем результат. Обращаемся к классу "Http_methods" и выбираем необходимый запрос "get" c указанием "url"
        result_get = Http_methods.get(get_url)

        # указываем кодировку ответа и выводим результат ответа в текстовом формате
        result_get.encoding = 'utf-8'
        print(result_get.text)

        # возвращаем result_get для использования результата в методе "test_create_new_book" файла test_booking.py
        return result_get

    """Метод для обновления данных в книге"""
    @staticmethod
    # Находим booking_id книги и передаем в метод update_new_book.
    def update_new_book(booking_id):
        # ресурс метода PUT
        put_resource = '/booking/'

        # полный URL запроса для обновления данных книги
        put_url = base_url + put_resource + str(booking_id)
        print(put_url)

        # обновляем информацию новой локации в json-формате
        json_for_update_new_book = {
            "firstname": "James",
            "lastname": "Smith",
            "totalprice": 599,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2023-01-01",
                "checkout": "2024-03-24"
            },
            "additionalneeds": "QA"
        }

        # Получаем результат. Обращаемся к классу "Http_methods" и выбираем необходимый метод put,
        # передавая URL, данные для обновления, а также username и password
        result_put = Http_methods.put(put_url, json_for_update_new_book, Http_methods.username, Http_methods.password)

        # указываем кодировку ответа и выводим результат ответа в текстовом формате
        result_put.encoding = 'utf-8'
        print(result_put.text)

        # возвращаем result_put для использования результата в методе "test_create_new_book" файла test_booking.py
        return result_put

    """Метод для удаления книги"""
    @staticmethod
    # Находим booking_id книги и передаем в метод delete_new_book.
    def delete_new_book(booking_id):
        # ресурс метода DEL
        del_resource = '/booking/'

        del_url = base_url + del_resource + str(booking_id)
        print(del_url)

        # указываем booking_id удаляемой книги в json-формате
        json_for_delete_new_book = {
            "booking_id": booking_id
        }

        # Получаем результат. Обращаемся к классу "Http_methods" и выбираем необходимый метод delete,
        # передавая URL, данные для обновления, а также username и password
        result_del = Http_methods.delete(del_url, json_for_delete_new_book, Http_methods.username,
                                         Http_methods.password)

        # указываем кодировку ответа и выводим результат ответа в текстовом формате
        result_del.encoding = 'utf-8'
        print(result_del.text)

        # возвращаем result_put для использования результата в методе "test_create_new_book" файла test_booking.py
        return result_del
