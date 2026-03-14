import os
from datetime import datetime
from features.history_manager import add_history
def open_file(path):
    """This function manages the openning a file and create a record format for opened files"""
    filename = os.path.basename(path)
    date = datetime.now().isoformat(sep=" ", timespec='seconds')
    new_record = {"filename":filename, "path": path, "date":date}
    add_history("opend files",new_record)
    os.startfile(path)
