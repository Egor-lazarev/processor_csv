import pytest


@pytest.fixture
def sample_data():
    return [
        {'name': 'Finn', 'age': '17', 'score': '85.5'},
        {'name': 'Jake', 'age': '28', 'score': '92.0'},
        {'name': 'BMO', 'age': '1006', 'score': '78.3'},
    ]


@pytest.fixture
def sample_csv_file(tmp_path):
    data = '''name,age,score
Finn,17,85.5
Jake,28,92.0
BMO,1006,78.3'''
    file = tmp_path / 'test.csv'
    file.write_text(data)
    return str(file)


@pytest.fixture
def empty_data():
    return []
