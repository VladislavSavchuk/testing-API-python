"""Подключение логирования"""
import datetime  # Импортируем модуль datetime для работы с датой и временем

import os  # Импортируем модуль os для работы с операционной системой

from requests import Response  # Импортируем класс Response из модуля requests


class Logger:
    # 'logs/log_' - файл будет храниться в папке logs, его имя начинается на log_
    # datetime.datetime.now() - используем библиотеку datetime и указываем настоящее время
    # .strftime('%Y-%m-%d_%H-%M-%S') - указываем формат даты и времени
    # '.log' - расширение файла
    file_name = f'logs/log_' + str(datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')) + '.log'

    """Метод для записи данных в лог-файл"""
    # Декоратор @classmethod преобразует обычный метод в метод класса. Это значит, что он привязан к самому классу,
    # а не к его экземплярам. Первым аргументом такого метода всегда является сам класс (обычно обозначается как cls),
    # а не экземпляр класса (self).
    @classmethod
    # cls - метод write_logs_to_file относится к классу Logger
    # data: str - данные помещаются в файл в виде строки
    def write_logs_to_file(cls, data: str):
        # Открываем лог-файл file_name в режиме дозаписи ('a') с кодировкой utf-8
        with open(cls.file_name, 'a', encoding='utf-8') as logger_file:
            # Записываем данные в лог-файл
            logger_file.write(data)

    """Метод для добавления информации о Запросе в лог-файл"""
    @classmethod
    # cls - метод add_request сможет обращаться к переменным класса Logger
    # url: str - URL в виде строки
    # method: str - название метода в виде строки
    def add_request(cls, url: str, method: str):
        # Получаем имя текущего теста из переменной окружения
        test_name = os.environ.get('PYTEST_CURRENT_TEST')
        # Формируем строки с данными о запросе, включая имя теста, дату и время, метод и URL
        data_to_add = f'\n-----\n'
        data_to_add += f"Test: {test_name}\n"
        data_to_add += f"Time: {str(datetime.datetime.now())}\n"
        data_to_add += f"Request method: {method}\n"
        data_to_add += f"Request URL: {url}\n"
        data_to_add += "\n"

        # Вызываем метод для записи данных запроса в лог-файл. Обращаемся к классу cls, методу write_logs_to_file
        # и передаем название переменной data_to_add
        cls.write_logs_to_file(data_to_add)

    """Метод для добавления информации Ответа на запрос в лог-файл"""
    @classmethod
    # cls - метод add_response относится к классу Logger
    # result: Response - указываем ответ запроса, для этого импотритруем класс Response из модуля requests
    def add_response(cls, result: Response):
        # Получаем куки и заголовки из переменной result ответа Response и преобразуем в словарь
        cookies_as_dict = dict(result.cookies)
        headers_as_dict = dict(result.headers)

        # Формируем строки с данными в ответе, включая статус-код, текст ответа, заголовки и куки
        data_to_add = f"Response code: {result.status_code}\n"
        data_to_add += f"Response text: {result.text}\n"
        data_to_add += f"Response headers: {headers_as_dict}\n"
        data_to_add += f"Response cookies: {cookies_as_dict}\n"
        data_to_add += f'\n-----\n'

        # Вызываем метод для записи данных ответа в лог-файл. Обращаемся к классу cls, методу write_logs_to_file
        # и передаем название переменной data_to_add
        cls.write_logs_to_file(data_to_add)
