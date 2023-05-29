from src import util
from src.util import output_date, description_of_transaction, sender_data, load_operations, reciever_data, money_amount, \
    currency


def test_load_operation():
    assert load_operations("tests/test_data.json") is not None
    assert type(load_operations("tests/test_data.json")) is list
    assert {} not in load_operations("tests/test_data.json")

def test_date():
    assert output_date({"date": "2019-04-18T11:22:18.800453"}) == "18.4.2019"

def test_description():
    assert description_of_transaction({"description": "Перевод с карты на карту"}) == "Перевод с карты на карту"

def test_sender_data():
    assert sender_data({}) == "Нет отправителя"
    assert sender_data({"from": "Maestro 1308795367077170"}) == "Maestro 1308 79** **** 7170"
    assert sender_data({"from": "Счет 46363668439560358409"}) == "Счет 4636 36** **** **** 8409"

def test_reciever_data():
    assert reciever_data({"to": "Счет 96527012349577388612"}) == "Счет  **8612"

def test_money_amount():
    assert money_amount({"operationAmount":{"amount": "74895.83"}}) == "74895.83"

def test_currency():
    assert currency({"operationAmount":{"currency":{"name": "руб."}}}) == "руб."