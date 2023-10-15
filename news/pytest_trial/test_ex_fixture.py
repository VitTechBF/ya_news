import pytest


@pytest.fixture  # Декоратор, обозначающий, что эта функция - фикстура.
def give_me_a_string():
    return 'Какой чудесный день!'  # Фикстура возвращает строку.

'''
# Если тестовой функции для работы нужна фикстура, 
# она указывается в параметрах.
def test_string_fixture(give_me_a_string):  
    # Переменная с именем фикстуры содержит в себе объект, 
    # который вернула фикстура.
    assert give_me_a_string[0] == 'К'  
'''

# Новая фикстура возвращает список со строкой из первой фикстуры.
@pytest.fixture
def pack_to_list(give_me_a_string):  # Фикстура может вызывать другие фикстуры.
    return [give_me_a_string]


# Тестовая функция использует обе фикстуры и проверяет их содержимое.
def test_string_fixture(pack_to_list, give_me_a_string):  
    assert pack_to_list == [give_me_a_string] 