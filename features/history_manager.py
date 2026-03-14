import json
from tabulate import tabulate
from utils.input_validator import Validator
def add_history(destnation,record):
    """ add a history records in to the history.json"""
    path='./data/history.json'
    Validator().history_validator(path)
    with open(path,'r') as file:
        history = json.load(file)
    history[destnation].append(record)
    with open(path, 'w') as file:
        json.dump(history,file, indent=4)
        print("History recorded!")

def display_history():
    """ This file display a history in a table format """
    try:
        path = "./data/history.json"
        with open(path, 'r') as file:
            histories = json.load(file)
    except json.decoder.JSONDecodeError as e:
        print(f"Error: History Not found.")
    except FileNotFoundError as e:
        print(f"Error: There is no recorded history yet.")
    else:
        for history in histories:
            print(f"\n{'='*80}\n||{history.center(77)}||\n{'='*80}")
            if not histories[history]:
                print("No record".center(77))
            print(tabulate(histories[history], headers="keys",tablefmt='fancy_grid'))