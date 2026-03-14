import json 
from tabulate import tabulate
def display_history():
    with open("./data/history.json", 'r') as f:
        data = json.load(f)
    for history in data:
        print(f"\n{'='*80}\n||{history.center(77)}||\n{'='*80}")
        print(tabulate(data[history], headers="keys",tablefmt='fancy_grid'))