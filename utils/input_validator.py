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





# print(dir(os))
# os.chdir('C:/Users/User/mikigithub/pdf_launcher')
# path = os.path.aos.path.join(os.getcwd(), )
# os.makedirs('core')
# os.rmdir('core')
# os.removedirs('core/miki')
# for dirpath, dirname, filenames in os.walk('C:/Users/User/mikigithub/pdf_launcher'):
#     print( filenames)
# created_at =os.stat('cli.py').st_atime
# print(datetime.datetime.fromtimestamp(created_at))
# print(os.path.splitext('C:/Users/User/mikigithub/pdf_launcher/cli.py'))
# os.open('C:/Users/User/mikigithub/pdf_launcher/cli.py')
