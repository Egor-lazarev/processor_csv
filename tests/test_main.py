import argparse
from unittest.mock import patch

import main


def test_main_with_aggregate(sample_csv_file):
    with patch(
        'argparse.ArgumentParser.parse_args',
        return_value=argparse.Namespace(
            file=sample_csv_file,
            where=None,
            aggregate='score=max'
        )
    ):
        with patch('main.aggregate_data', return_value=[{'max': 92.0}]):
            with patch('main.tabulate') as mock_tabulate:
                mock_tabulate.return_value = 'mock_table'
                with patch('builtins.print') as mock_print:
                    main.main()
                    mock_print.assert_called_with('mock_table')


def test_main_with_filter(sample_csv_file):
    with patch(
        'argparse.ArgumentParser.parse_args',
        return_value=argparse.Namespace(
            file=sample_csv_file,
            where='age>25',
            aggregate=None
        )
    ):
        with patch('main.filter_data', return_value=[{'name': 'Jake'}]):
            with patch('main.tabulate') as mock_tabulate:
                mock_tabulate.return_value = 'filtered_table'
                with patch('builtins.print') as mock_print:
                    main.main()
                    mock_print.assert_called_with('filtered_table')


def test_main_no_data_after_filter(sample_csv_file):
    with patch(
        'argparse.ArgumentParser.parse_args',
        return_value=argparse.Namespace(
            file=sample_csv_file,
            where='age>2000',
            aggregate=None
        )
    ):
        with patch('main.filter_data', return_value=[]):
            with patch('builtins.print') as mock_print:
                main.main()
                mock_print.assert_called_with(
                    'Нет данных, соответствующих условию запроса'
                )


def test_main_basic_output(sample_csv_file):
    with patch(
        'argparse.ArgumentParser.parse_args',
        return_value=argparse.Namespace(
            file=sample_csv_file,
            where=None,
            aggregate=None
        )
    ):
        with patch('main.tabulate') as mock_tabulate:
            mock_tabulate.return_value = 'basic_table'
            with patch('builtins.print') as mock_print:
                main.main()
                mock_print.assert_called_with('basic_table')
