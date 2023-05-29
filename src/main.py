from datetime import datetime
from src.util import load_operations, output_date, description_of_transaction, sender_data, reciever_data, money_amount, \
    currency

if __name__ == '__main__':
    filename = 'operations.json'
    operation = load_operations(filename)

    sort_data = sorted(operation, key=lambda k: '.'.join(k['date'].split('.')))


    final_operation = sort_data[-6:]

    for word in final_operation:

        if word["state"] == "EXECUTED":
            print(output_date(word), description_of_transaction(word))
            print(sender_data(word), "->", reciever_data(word))
            print(money_amount(word), currency(word), end='\n\n')
        else:
            pass