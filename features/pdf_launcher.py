import os
import json
from datetime import datetime
new_data = {"name":"miki", "age": 20, "address":"Addis"}
def open_file(path):
    print(path)
    filename = os.path.basename(path)
    opend_at = datetime.now().isoformat(sep=" ", timespec='seconds')
    new_record = {"filename":filename, "path": path, "opend-at":opend_at}
    with open('./data/history.json', 'r') as f:
        history =json.load(f)
    history["opend_files"].append(new_record)
    with open('./data/history.json', 'w') as f:
        json.dump(history, f)
    print(history)
    os.startfile(path)
