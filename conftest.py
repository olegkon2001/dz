import pytest


@pytest.fixture
def test_url():
    return 'https://file.notion.so/f/s/d22c7143-d55e-4f1d-aa98-e9b15e5e5efc/operations.json?spaceId=0771f0bb-b4cb-4a14-bc05-94cbd33fc70d&table=block&id=f11058ed-10ad-42ea-a13d-aad1945e5421&expirationTimestamp=1676548733323&signature=mTg0H5jJKcBTEiWSTslM3NtnCrAhdAlsV0kL5RwKIyI&downloadName=operations.json '

@pytest.fixture
def test_data():
    return [{'date': '2019-08-26T10:50:50.294041',
  'description': 'Перевод организации',
  'from': 'Maestro 1596837868705199',
  'id': 441945886,
  'operationAmount': {'amount': '31957.58',
                      'currency': {'code': 'USD', 'name': 'USD'}},
  'to': 'Счет 64686473678894779589'},
 {'date': '2020-07-03T18:35:29.512364',
  'from': 'MasterCard 7158300734726758',
  'id': '41428829',
  'operationAmount': {'amount': '8221.37',
                      'currency': {'code': 'USD', 'name': 'USD'}},
  'state': 'EXECUTED',
  'to': 'Счет 35383033474447895560'},
 {'date': '2018-06-30T02:08:58.425572',
  'description': 'Перевод организации',
  'from': 'Счет 75106830613657916952',
  'id': 587085106,
  'operationAmount': {'amount': '9824.07',
                      'currency': {'code': 'USD', 'name': 'USD'}},
  'state': 'EXECUTED',
  'to': 'Счет 35383033474447895560'},
 {'date': '2018-03-23T10:45:06.972075',
  'description': 'Открытие вклада',
  'from': 'Счет 11776614605963066702',
  'id': 939719570,
  'operationAmount': {'amount': '48223.05',
                      'currency': {'code': 'USD', 'name': 'USD'}}}]







