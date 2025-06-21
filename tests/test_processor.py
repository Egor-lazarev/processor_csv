import pytest

from processor import (
    aggregate_data,
    _is_numeric_column,
    filter_data,
    parse_condition,
    read_csv_to_dict_list,
)


def test_read_csv_to_dict_list(sample_csv_file):
    result = read_csv_to_dict_list(sample_csv_file)
    assert isinstance(result, list), 'Результат должен быть списком словарей'
    assert len(result) > 0, 'Файл не должен быть пустым'
    assert all(
        key in result[0] for key in ['name', 'age', 'score']
    ), 'Должны быть все ожидаемые колонки'


def test_filter_data_numeric_operations(sample_data):
    result = filter_data(sample_data, 'age', '>', '20')
    assert len(result) == 2, 'Фильтрация работает некорректно'
    assert {r['name'] for r in result} == {'Jake', 'BMO'}, \
        'Фильтрация работает некорректно'

    result = filter_data(sample_data, 'age', '<=', '28')
    assert len(result) == 2, 'Фильтрация работает некорректно'
    assert {r['name'] for r in result} == {'Finn', 'Jake'}, \
        'Фильтрация работает некорректно'


def test_filter_data_string_operations(sample_data):
    result = filter_data(sample_data, 'name', '==', 'BMO')
    assert len(result) == 1, 'Фильтрация работает некорректно'
    assert result[0]['age'] == '1006', 'Фильтрация работает некорректно'

    result = filter_data(sample_data, 'name', '!=', 'BMO')
    assert len(result) == 2, 'Фильтрация работает некорректно'


def test_filter_data_invalid_operator(sample_data):
    with pytest.raises(ValueError, match='Неизвестный оператор'):
        filter_data(sample_data, 'age', '??', '25')


def test_aggregate_data_operations(sample_data):
    result = aggregate_data(sample_data, 'score', 'max')
    assert result == [{'max': 92.0}], \
        'Агрегирующая функция max работает некорректно'

    result = aggregate_data(sample_data, 'score', 'min')
    assert result == [{'min': 78.3}], \
        'Агрегирующая функция min работает некорректно'

    result = aggregate_data(sample_data, 'score', 'avg')
    assert result[0]['avg'] == pytest.approx((85.5 + 92.0 + 78.3) / 3), \
        'Агрегирующая функция avg работает некорректно'


def test_aggregate_empty_data(empty_data):
    result = aggregate_data(empty_data, 'score', 'max')
    assert result == []


def test_aggregate_non_numeric_column(sample_data):
    with pytest.raises(ValueError, match='должна быть числовой'):
        aggregate_data(sample_data, 'name', 'max')


def test_parse_condition():
    assert parse_condition('age>25') == ('age', '>', '25')
    assert parse_condition('score<=85.5') == ('score', '<=', '85.5')
    assert parse_condition('name==BMO') == ('name', '==', 'BMO')
    assert parse_condition('age = 30') == ('age', '=', '30')


def test_parse_invalid_condition():
    with pytest.raises(ValueError, match='Недопустимый формат'):
        parse_condition('invalid_condition')


def test_is_numeric_column(sample_data):
    assert _is_numeric_column('age', sample_data), \
        'Колонка должна содержать числовое значение'
    assert not _is_numeric_column('name', sample_data), \
        'Колонка должна содержать строку'
