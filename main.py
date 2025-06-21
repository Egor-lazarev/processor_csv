import argparse
from tabulate import tabulate

from processor import (
    aggregate_data,
    filter_data,
    parse_condition,
    read_csv_to_dict_list
)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', required=True, help='Путь или имя csv файла')
    parser.add_argument('--where', help='Фильтрация по колонке')
    parser.add_argument('--aggregate', help='Агрегирующие операции')
    args = parser.parse_args()

    data = read_csv_to_dict_list(args.file)

    if args.where:
        column, operator, value = parse_condition(args.where)
        data = filter_data(data, column, operator, value)
        if not data:
            print('Нет данных, соответствующих условию запроса')
            return

    if args.aggregate:
        column, _, operation = parse_condition(args.aggregate)
        result = aggregate_data(data, column, operation)
        print(tabulate(result, headers='keys', tablefmt='grid'))
    else:
        print(tabulate(data, headers='keys', tablefmt='grid'))


if __name__ == '__main__':
    main()
