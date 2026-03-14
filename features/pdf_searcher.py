import os
import json
import glob
from datetime import datetime
from tabulate import tabulate

def filter_pdf(path):
    filter_path=f'{path}/**/*.pdf'
    files = glob.glob(filter_path,recursive=True)
    cols = ["No", "File name", "Path"]
    rows =[]
    for role, filepath in enumerate(files, 1):
        filename = os.path.basename(filepath)
        rows.append([role, filename, filepath])
    print(tabulate(rows,cols,tablefmt="fancy_grid"))
    search_time = datetime.now().isoformat(sep=' ', timespec='seconds')
    new_record = {"path":path,"date":search_time}
    with open('./data/history.json', 'r') as f:
        history = json.load(f)
    history["search_history"].append(new_record)
    with open('./data/history.json','w') as f:
        json.dump(history, f)