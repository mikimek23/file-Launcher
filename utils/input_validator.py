import os
import json
class Validator:
    def file_validator(self,path):
        """ This function check if the file path is correct and the extantion of the file"""
        
        if not os.path.exists(path):
            raise ValueError(f"The specified path does not exist.\nPath: {path}")
        if not os.path.isfile(path):
            raise ValueError(f"Please provide a valid PDF file path.\nPath: {path}")
        ext = os.path.splitext(path)[1]
        if ext.lower() !='.pdf':
            raise ValueError(f"please provide a valid PDF file path.\nPath: {path}")
        return True
    
    def dir_validator(self, path):
        """ This function validate if the provided path is exist or not"""

        if not os.path.exists(path):
            raise ValueError(f"The specified path does not exist.\nPath: {path}")
        if not os.path.isdir(path):
            raise ValueError(f"Please provide a valid folder path.\nPath: {path}")
        return True
    
    def history_validator(self, path):
        """ This function validate the existance of data/history and create one if not"""

        file_path = os.path.abspath(path)
        dir_path = os.path.split(file_path)[0]
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
            print("file created")
        if not os.path.exists(file_path):
            with open(file_path, 'w') as file:
                data = json.dumps({"opend files":[], "search history":[]},indent=4)
                file.write(data)
        if os.path.getsize(file_path)==0:
             with open(file_path, 'w') as file:
                data = json.dumps({"opend files":[], "search history":[]},indent=4)
                file.write(data)