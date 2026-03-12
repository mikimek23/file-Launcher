import argparse
import os
def cli_parser():
    parser = argparse.ArgumentParser(description="PDF Launcher CLI Tool")
    commands = parser.add_subparsers(dest='command', help="availeble commands", required=True)
    open_pdf = commands.add_parser('open', help='open a file')
    open_pdf.add_argument('path', metavar='filename',type=os.path.abspath, help='the name of the file to open')
    search_pdf = commands.add_parser('search',help='search all pdf files from a folder')
    search_pdf.add_argument('path', metavar='filename', type=os.path.abspath, help='the path of the folder to search')
    commands.add_parser('recent', help='to see the history')
    user_input = parser.parse_args()
    arg_value = getattr(user_input, 'path', None)
    return user_input.command, arg_value