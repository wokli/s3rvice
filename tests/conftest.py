'''
Конфиг тестов
'''
import pytest
from s3rvice import application
from s3rvice.model import Model

@pytest.yield_fixture
def app():
    '''
    Фикструра для пробрасывания аппа в тесты
    '''
    yield application

@pytest.yield_fixture
def model():
    '''
    Фикстура для модели
    '''
    yield Model()

