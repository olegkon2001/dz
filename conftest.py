import pytest


@pytest.fixture
def test_url():
    return "https://s3.us-west-2.amazonaws.com/secure.notion-static.com/d22c7143-d55e-4f1d-aa98-e9b15e5e5efc" \
                    "/operations.json?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz" \
                    "-Credential=AKIAT73L2G45EIPT3X45%2F20230208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date" \
                    "=20230208T131534Z&X-Amz-Expires=86400&X-Amz-Signature" \
                    "=4cd83dd9ab064d1ed2695b2117a467d14bced9d36853e35910890093ed7b4ae3&X-Amz-SignedHeaders=host" \
                    "&response-content-disposition=filename%3D%22operations.json%22&x-id=GetObject "

@pytest.fixture
def test_data():
    return [{'data': '2019-08-26T10:50:50.294041',
             'description': 'Перевод организации',
             'from': 'Maestro 1596837868705199',
             'id': 441945886,
             "operationAmount": {'amount': '31957.58',
                                 'currency': {'code': 'USD', 'name': 'USD'}},
     'to': 'Счет 64686473678894779589'},
    {'date': '2020-07-03T18:35:29.512364',
     'from': 'MasterCard 7158300734726758',
     'id': '41428829',
     'operationAmount': {"amount":'8221.37',
                         'currency': {'code': 'USD', 'name': 'USD'}},
     'state': 'EXECUTED',
     'to': 'Счет 35383033474447895560'},
    {'date': '2018-06-30T02:08:58.425572',
     'description': 'Перевод организации',
     'from': 'Счет 75106830613657916952',
     'id': 587085106,
     "operationAmount": {'amount': '9824.07',
                         'currency': {'code': 'USD', 'name': 'USD'}},
     'state': 'EXECUTED',
     'to': 'Счет 35383033474447895560'},
            {'date': '2018-03-23T10:45:06.972075',
             'description': 'Открытие вклада',
             'from': 'Счет 11776614605963066702',
             'id': 939719570,
             "operationAmount": {'amount': '48223.05',
                                 'currency': {'code': 'USD', 'name': 'USD'}},
             'state': 'EXECUTED',
             'to': 'Счет 35383033474447895560'},
            {'date': '2019-04-04T23:20:05.206878',
             'description': 'Перевод организации',
             'from': 'Счет 41421565395219882431',
             'id': 142264268,
             "operationAmount": {'amount': '79114.93',
                                 'currency': {'code': 'USD', 'name': 'USD'}}}]







