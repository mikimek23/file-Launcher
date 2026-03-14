import os
from datetime import datetime
from features.history_manager import add_history
new_data = {"name":"miki", "age": 20, "address":"Addis"}
def open_file(path):
    filename = os.path.basename(path)
    date = datetime.now().isoformat(sep=" ", timespec='seconds')
    new_record = {"filename":filename, "path": path, "date":date}
    add_history("opend files",new_record)
    os.startfile(path)
