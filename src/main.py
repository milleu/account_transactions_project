
from src.util import load_operations, output_date, description_of_transaction, sender_data, reciever_data, money_amount, \
    currency

if __name__ == '__main__':
    filename = 'operations.json'
    operation = load_operations(filename)
    final_operation = operation[:5]

    for word in final_operation:

        if word["state"] == "EXECUTED":
            print(output_date(word), description_of_transaction(word))
            print(sender_data(word), "->", reciever_data(word))
            print(money_amount(word), currency(word), end='\n\n')
        else:
            pass