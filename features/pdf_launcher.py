import os
import json
from datetime import datetime
from features.history_manager import add_history
new_data = {"name":"miki", "age": 20, "address":"Addis"}
def open_file(path):
    filename = os.path.basename(path)
    opend_at = datetime.now().isoformat(sep=" ", timespec='seconds')
    new_record = {"filename":filename, "path": path, "opend-at":opend_at}
    add_history(new_record)
    # with open('./data/history.json', 'r') as f:
    #     history =json.load(f)
    # history["opend_files"].append(new_record)
    # with open('./data/history.json', 'w') as f:
    #     json.dump(history, f)
    os.startfile(path)
