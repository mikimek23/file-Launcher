import os

class Validator:
    def file_validator(self,path):
        if not os.path.exists(path):
            raise ValueError(f"The specified path does not exist.\nPath: {path}")
        if not os.path.isfile(path):
            raise ValueError(f"Please provide a valid PDF file path.\nPath: {path}")
        ext = os.path.splitext(path)[1]
        if ext.lower() !='.pdf':
            raise ValueError(f"please provide a valid PDF file path.\nPath: {path}")
        return True
    def dir_validator(self, path):
        if not os.path.exists(path):
            raise ValueError(f"The specified path does not exist.\nPath: {path}")
        if not os.path.isdir(path):
            raise ValueError(f"Please provide a valid folder path.\nPath: {path}")
        return True