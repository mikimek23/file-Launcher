import os
import json
import glob
from datetime import datetime
from tabulate import tabulate
from features.history_manager import add_history

def filter_pdf(path:str)->None:
    """ This function manages scanning a folder and creating a record format for search history"""
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
    add_history( "search history", new_record)