from cli import cli_parser
from utils.input_validator import Validator
from features.pdf_launcher import open_file
from features.pdf_searcher import filter_pdf
command, path = cli_parser()
if (command== 'open'):
    try:
        Validator().file_validator(path)
        open_file(path)
    except ValueError as e:
        print('Error:',e)
if(command == 'search'):
    try:
        Validator().dir_validator(path)
        filter_pdf(path)
    except ValueError as e:
        print('Error:',e)
if(command == 'recent'):
    print('I will show your history')

