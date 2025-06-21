import csv


def read_csv_to_dict_list(file_path):
    with open(file_path, mode='r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        data = [row for row in csv_reader]

    return data


def filter_data(data, column, operator, value):

    filtered_rows = []
    valid_operators = ['>', '<', '>=', '<=', '!=', '==', '=']

    if operator not in valid_operators:
        raise ValueError(f'Неизвестный оператор: {operator}')

    for row in data:
        try:
            item = row[column]

            if _is_numeric_column(column, data):
                item = float(item)
                compare_value = float(value)
            else:
                compare_value = value

            if operator == '>' and item > compare_value:
                filtered_rows.append(row)
            elif operator == '<' and item < compare_value:
                filtered_rows.append(row)
            elif operator == '>=' and item >= compare_value:
                filtered_rows.append(row)
            elif operator == '<=' and item <= compare_value:
                filtered_rows.append(row)
            elif operator == '!=' and item != compare_value:
                filtered_rows.append(row)
            elif operator in ['==', '='] and item == compare_value:
                filtered_rows.append(row)

        except (ValueError, KeyError):
            continue

    return filtered_rows


def aggregate_data(data, column, operation):

    if not data:
        return []

    if not _is_numeric_column(column, data):
        raise ValueError(
            f'Колонка "{column}" должна быть числовой для агрегации'
        )

    numeric_values = [float(row[column]) for row in data]

    if operation == 'max':
        result = max(numeric_values)
    elif operation == 'min':
        result = min(numeric_values)
    elif operation == 'avg':
        result = sum(numeric_values) / len(numeric_values)
    else:
        raise ValueError(f'Неизвестная операция: {operation}')

    return [{operation: result}]


def parse_condition(condition_str):

    operators = ['>=', '<=', '==', '!=', '>', '<', '=']

    for operator in operators:
        if operator in condition_str:
            column, value = condition_str.split(operator, 1)
            return column.strip(), operator, value.strip()
    raise ValueError(f'Недопустимый формат: {condition_str}')


def _is_numeric_column(column, data):
    return all(_is_convertible_to_float(row[column]) for row in data)


def _is_convertible_to_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False
