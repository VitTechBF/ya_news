'''
# test_example.py
import pytest


pytestmark = pytest.mark.skip  # Все тесты в этом файле будут пропущены.



def one_more(x):
    return x + 1


def test_correct():
    assert one_more(4) == 5


def test_fail():
    with pytest.raises(AssertionError):
        assert one_more(3) == 5


def division(dividend, divisor):
    return dividend / divisor


def test_zero_division():
    with pytest.raises(ZeroDivisionError):  # Ожидается ошибка деления на 0.
        # При вызове функции с такими аргументами возникнет ошибка.
        result = division(1, 0)
    
def get_sort_list(string):
    new_list = sorted(string.split(', '))  # Сортируем список.
    return new_list

def test_sort():
    """Тестируем функцию get_sort_list()."""
    result = get_sort_list('Яша, Саша, Маша, Даша')
    assert result == ['Даша', 'Маша', 'Саша', 'Яша'] 



old_version = True

@pytest.mark.skipif(
    "sys.version_info > (2, 7)",
    reason='Только для старых версий Python'
)
def test_for_old_versions():
    assert old_version == True

# test_example.py
def one_more(x):
    return x + 1


def get_sort_list(str):
    new_list = sorted(str.split(', '))
    return new_list


def test_correct():
    print('Правильный тест')  # Новая строка.
    assert one_more(4) == 5


@pytest.mark.skip(reason='Что-то не работает')  # Маркер.
def test_fail():
    print('Неправильный тест')  # Новая строка.
    assert one_more(3) == 5


def test_sort():
    """Тестируем функцию get_sort_list()."""
    result = get_sort_list('Яша, Саша, Маша, Даша')
    assert result == ['Даша', 'Маша', 'Саша', 'Яша']

def test_type():
    """Тестируем тип данных, возвращаемых из get_sort_list()."""
    result = get_sort_list('Яша, Саша, Маша, Даша')
    # Провальный тест:
    # ожидаем число, но вернётся список.
    assert isinstance(result, int)  

@pytest.mark.xfail(reason='Пусть пока падает, завтра починю.')
def test_false():
    assert False 

@pytest.mark.xfail("sys.version_info < (2, 1)", 
                   reason='Это старая версия Python, чего же вы ждали!')
def test_for_new_python():
    # Тест, который провалится на старых версиях Python.
    ... 
'''
# test_example.py

import pytest 
# Импортируем новую функцию.
from time import sleep

def one_more(x):
    return x + 1

@pytest.mark.slow  # Отмечаем маркером тест.
def test_type():
    """Тестируем тип данных, возвращаемых из get_sort_list()."""
    sleep(3)  # Трёхсекундная пауза.

@pytest.mark.parametrize(
    'input_arg, expected_result',
    [
        (4, 5), 
        pytest.param(3, 5, marks=pytest.mark.xfail)  # Ожидается падение теста.
    ],
    ids=['First parameter', 'Second parameter',]
)
def test_one_more(input_arg, expected_result):  # Те же параметры, что и в декораторе.
    assert one_more(input_arg) == expected_result

def cartesian_product(a, b):
    return a * b

@pytest.mark.slowww  # Название маркера с опечаткой.
def test_type():
    """Тестируем тип данных, возвращаемых из get_sort_list()."""
    ... 

@pytest.mark.parametrize('x', [1, 2])
@pytest.mark.parametrize('y', ['one', 'two'])
def test_cartesian_product(x, y):
    assert cartesian_product(x, y) is not None