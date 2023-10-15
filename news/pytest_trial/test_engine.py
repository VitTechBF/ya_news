# test_engine.py
'''
import pytest

# Импортируем класс двигателя.
from engine_class import Engine


@pytest.fixture
def engine():
    """Фикстура возвращает экземпляр класса двигателя."""
    return Engine()


# Эта фикстура не возвращает никаких значений, но изменяет объект,
# созданный другой фикстурой.
@pytest.fixture
def start_engine(engine):  # Вызываем фикстуру получения объекта двигателя.
    """Фикстура запускает двигатель."""
    # Изменяем значение свойства объекта:
    engine.is_running = True


def test_engine_is_running(engine, start_engine):  # Вызываем обе фикстуры.
    """Тест проверяет, работает ли двигатель."""
    assert engine.is_running  # Проверяем, что значение атрибута is_running это True.


import pytest

from engine_class import Engine


@pytest.fixture(scope='session')
def engine():
    """Фикстура возвращает экземпляр класса двигателя."""
    print('Engine factory')
    return Engine()


@pytest.fixture(autouse=True)
def start_engine(engine):
    """Фикстура запускает двигатель."""
    engine.is_running = True  # Запустим двигатель.
    # Распечатаем строчку до выполнения теста.
    print(f'Before test engine.is_running {engine.is_running}') 
    yield  # В этот момент начинает выполняться тест.
    engine.is_running = False  # Заглушим двигатель.
    # Распечатаем строчку после выполнения теста и остановки двигателя.
    print(f'After test engine.is_running {engine.is_running}') 


def test_engine_is_running(engine):  
    """Тест проверяет, работает ли двигатель."""
    print('test_engine_is_running')  # Выведем название теста.
    assert engine.is_running


def test_check_engine_class(engine):
    """Тест проверяет класс объекта."""
    print('test_check_engine_class')  # Выведем название теста.
    assert isinstance(engine, Engine) 
'''
# test_engine.py
from engine_class import Engine


def test_engine_is_running(engine):  
    """Тест проверяет, работает ли двигатель."""
    assert engine.is_running


def test_check_engine_class(engine):
    """Тест проверяет класс объекта."""
    assert isinstance(engine, Engine)