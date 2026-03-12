import os
import json
import glob
from datetime import datetime

def filter_pdf(path):
    filter_path=f'{path}/**/*.pdf'
    files = glob.glob(filter_path,recursive=True)
    print(f"{'filename'.center(86)}| {'path'.center(82)}")
    print('_'*200,'\n')
    for role, filepath in enumerate(files, 1):
        filename = os.path.basename(filepath)
        print(f"{role:0>2}. {filename:<82}| {filepath:<82}")
    search_time = datetime.now().isoformat(sep=' ', timespec='seconds')
    new_record = {"path":path,"date":search_time}
    with open('./data/history.json', 'r') as f:
        history = json.load(f)
    history["search_history"].append(new_record)
    with open('./data/history.json','w') as f:
        json.dump(history, f)
        print(history["search_history"])