"""Тестирование API запросов для Booking"""

# импортируем json для преобразования ответа
import json

# импортируем класс Booking из файла api.py папки utils
from utils.api import Booking

# импортируем класс Checking из файла checking.py папки utils
from utils.checking import Checking

# импортируем класс Response из стандартной библиотеки requests
from requests import Response

"""Создание, изменение и удаление новой книги"""


class Test_new_book:
    def test_create_new_book(self):
        """Создание токена"""
        print('Метод POST. Token creation')
        # Обращаемся к классу Booking и вызываем метод create_new_token.
        # Присваиваем ответ Response переменной result_token
        result_token: Response = Booking.create_new_token()

        # Проверка статус-кода
        Checking.check_status_code(result_token, 200)

        # Преобразуем ответ result_token в формат json.
        tokens = json.loads(result_token.text)

        # Выводим список ключей в ответе переменной tokens.
        print(f'List of keys in response: {list(tokens)}')

        # Проверяем наличие обязательных ключей в ответе. Обращаемся к классу Checking и вызываем метод check_json_token
        # Передаем ответ result_token и ожидаемые ключи в ответе
        Checking.check_json_token(result_token, ['token'])
        print()

        """Создание новой книги"""
        print('Метод POST. Creation of a new book')
        # Обращаемся к классу Booking и вызываем метод create_new_book.
        # Присваиваем ответ Response переменной result_post
        result_post: Response = Booking.create_new_book()

        # Сохраняем данные ответа в json-формате в переменной check_post
        check_post = result_post.json()

        # Получаем значение ключа bookingid из переменной check_post (либо ключ будет не найден) и присваиваем
        # переменной booking_id
        booking_id = check_post.get('bookingid', 'The key not found')

        # Проверка статус-кода ответа result_post. Обращаемся к классу Checking и вызываем метод check_status_code.
        # Передаем ответ result_post и указываем ожидаемый статус код в ответе (200)
        Checking.check_status_code(result_post, 200)

        # Преобразуем ответ result_post в формат json и присваиваем переменной tokens.
        tokens = json.loads(result_post.text)

        # Выводим список ключей в ответе переменной tokens.
        print(f'List of keys in response: {list(tokens)}')

        # Проверяем наличие обязательных ключей в ответе. Обращаемся к классу Checking и вызываем метод check_json_token
        # Передаем ответ result_post и ожидаемые ключи в ответе
        Checking.check_json_token(result_post, ['bookingid', 'booking'])

        # Проверяем наличие ключей внутри ключа 'booking' в ответе. Обращаемся к классу Checking и вызываем
        # метод check_json_token_booking. Передаем ответ result_post и ожидаемые ключи внутри ключа 'booking' в ответе
        Checking.check_json_token_booking(result_post, ['firstname', 'lastname', 'totalprice',
                                                        'depositpaid', 'bookingdates', 'additionalneeds'])

        # Проверяем значения обязательных полей в ответе.
        # Проверяем поле 'bookingid' в ответе. Обращаемся к классу Checking и вызываем метод check_info_booking_id.
        # Передаем ответ result_post и его ожидаемый ключ
        Checking.check_info_booking_id(result_post, 'bookingid')

        # Проверка значений полей 'firstname' и 'lastname' в ответе.
        # Обращаемся к классу Checking и вызываем метод check_json_value_in_booking.
        # Передаем ответ result_post и его ожидаемые ключ и значение в ответе
        Checking.check_json_value_in_booking(result_post, 'firstname', 'James')
        Checking.check_json_value_in_booking(result_post, 'lastname', 'Smith')

        # Проверяем поле 'totalprice' в ответе.
        Checking.check_json_value_in_booking(result_post, 'totalprice', 999)

        # Проверяем поле 'depositpaid' в ответе.
        Checking.check_json_value_in_booking(result_post, 'depositpaid', False)

        #  Проверяем поле 'additionalneeds' в ответе.
        Checking.check_json_value_in_booking(result_post, 'additionalneeds', 'QA')
        print()

        """Изменение данных в книге"""
        print('Метод PUT. Update of a new book.')
        # Обращаемся к классу Booking, вызываем метод update_new_book и передаем в него booking_id книги.
        # Присваиваем ответ Response переменной result_put
        result_put: Response = Booking.update_new_book(booking_id)

        # Проверка статус-кода. Обращаемся к классу Checking и вызываем метод check_status_code
        # Передаем ответ result_put и его ожидаемый статус код в ответе (200)
        Checking.check_status_code(result_put, 200)

        # Преобразуем ответ result_put в формат json.
        tokens = json.loads(result_put.text)

        # Выводим список ключей в ответе переменной tokens.
        print(f'Список ключей в ответе: {list(tokens)}')

        # Проверяем наличие обязательных ключей в ответе. Обращаемся к классу Checkin и вызываем метод check_json_token
        # Передаем ответ result_put и ожидаемые ключи в ответе
        Checking.check_json_token(result_put, ['firstname', 'lastname', 'totalprice',
                                               'depositpaid', 'bookingdates', 'additionalneeds'])
        print()

        """Проверка изменения данных в книге"""
        print('Метод GET. Checking for changes to the data in the book')
        # Обращаемся к классу Booking, вызываем метод get_new_book и передаем в него booking_id книги.
        # Присваиваем ответ Response переменной result_get
        result_get: Response = Booking.get_new_book(booking_id)

        # Проверка статус-кода
        Checking.check_status_code(result_get, 200)

        # Преобразуем ответ result_post в формат json.
        tokens = json.loads(result_get.text)

        # Выводим список ключей в ответе переменной result_get.
        print(f'List of keys in response: {list(tokens)}')

        # Проверяем наличие обязательных ключей в ответе. Обращаемся к классу Checkin и вызываем метод check_json_token
        # Передаем ответ result_get и ожидаемые ключи в ответе
        Checking.check_json_token(result_get, ['firstname', 'lastname', 'totalprice',
                                               'depositpaid', 'bookingdates', 'additionalneeds'])
        # Проверяем поле 'totalprice' в ответе, т.к. в нем было внесено изменение.
        Checking.check_json_value(result_get, 'totalprice', 599)

        # Проверяем поле 'depositpaid' в ответе, т.к. в нем было внесено изменение.
        Checking.check_json_value(result_get, 'depositpaid', True)
        print()

        """Удаление новой книги"""
        print('Метод DELETE. Deleting a new book')
        # Обращаемся к классу Booking, вызываем метод delete_new_book и передаем в него booking_id книги.
        # Присваиваем ответ Response переменной result_del
        result_del: Response = Booking.delete_new_book(booking_id)

        # Проверка статус-кода
        Checking.check_status_code(result_del, 201)

        # Проверяем значения обязательного поля после удаления. Обращаемся к классу Checking и вызываем
        # метод check_search_word_in_value. Передаем ответ result_del и его ожидаемое значение в ответе
        Checking.check_search_word_in_value(result_del, 'Created')
        print()

        """Проверка удаления книги"""
        print('Метод GET. Checking deleting a new book')
        # Обращаемся к классу Booking, вызываем метод get_new_book и передаем в него booking_id книги.
        # Присваиваем ответ Response переменной result_get
        result_get: Response = Booking.get_new_book(booking_id)

        # Проверка статус-кода
        Checking.check_status_code(result_get, 404)
        print()
