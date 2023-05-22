import json
from datetime import datetime


def load_operations(filename):
    """открываем файл, а также убираем чтение пустых словарей"""
    with open(filename, "r") as file:
        data = json.load(file)
        new_line = []
        for item in data:
            if item != {}:
                new_line.append(item)
        return new_line

def output_date(word):
    """считываем дату в необходимом формате (ДД.ММ.ГГГГ)"""
    actual_date = word["date"]
    thedate = datetime.fromisoformat(actual_date)
    return f"{thedate.day}.{thedate.month}.{thedate.year}"


def description_of_transaction(word):
    """выводит описание транзакции"""
    transaction_description = word["description"]
    return transaction_description


def sender_data(word):
    """показывает данные отправителя"""

    try:
        sender_info = word["from"]
        sender = sender_info.split(" ")
        card_number = sender[-1]
        if len(card_number) == 16:
          send_num = f"{''.join(sender[:-1])} {card_number[0:4]} {card_number[4:6]}** **** {card_number[-4:]}"
          word['from'] = send_num
          return send_num
        else:
          send_num = f"{''.join(sender[:-1])} {card_number[0:4]} {card_number[4:6]}** **** **** {card_number[-4:]}"
          word['from'] = send_num
          return send_num
    except KeyError:
      return "Нет отправителя"

def reciever_data(word):
    """показывает данные получателя"""

    try:
        reciever_info = word["to"]
        reciever = reciever_info.split(" ")
        card_number = reciever[-1]
        reciever_num = f"{''.join(reciever[:-1])}  **{card_number[-4:]}"
        word["to"] = reciever_num
        return reciever_num
    except KeyError:
      return "Нет получателя"

def money_amount(word):
    try:
        amount = word["operationAmount"]
        return amount["amount"]
    except KeyError:
      pass

def currency(word):
    currency = word["operationAmount"]
    currency_code = currency["currency"]
    return currency_code["name"]