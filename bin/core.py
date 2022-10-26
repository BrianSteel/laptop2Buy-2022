from os import path, remove, rmdir, listdir, mkdir
import requests
from datetime import datetime
from dateutil import parser

from bin.helper import printAll

FOLDER_ENDING = 'HTML files'
DATE_FILE = 'Date-Timestamp.txt'

def get_request_from_link(folder_parent_path, page, link, identifier, link_to_page_connector):
    if page:
        file_name = 'file-' + page + '.txt'
    else: 
        file_name = 'file-1' + '.txt'
    folder_path = path.join(folder_parent_path, identifier + FOLDER_ENDING)

    # folder_path is the full folder path, identifier + FOLDER_ENDING is the relative path
    if not path.isdir(identifier + FOLDER_ENDING): 
        mkdir(folder_path)

    file_path = path.join(folder_path, file_name)

    if path.exists(file_path) and path.getsize(file_path) > 0:
        req = open(file_path, 'r', encoding="utf-8")
        return req
    else:
        if page:
            req_link = link + link_to_page_connector + page
        else: 
            req_link = link
        req = requests.get(req_link).text
        file = open(file_path, 'w', encoding="utf-8")
        file.write(req)
        file.close()
        return req

def delete_last_file(identifier, page):
    file_name = 'file-' + page + '.txt'
    relative_folder_path = identifier + FOLDER_ENDING
    file_path = path.join(relative_folder_path, file_name)

    if path.isdir(relative_folder_path) and path.isfile(file_path):
        remove(file_path)

def delete_specific_folder(identifier):
    relative_folder_path = identifier + FOLDER_ENDING

    if path.isdir(relative_folder_path):
        for file in listdir(relative_folder_path):
            file_path = path.join(relative_folder_path, file)
            remove(file_path)
        rmdir(relative_folder_path)


def should_make_new_link_req():
    if path.isfile(DATE_FILE) and path.getsize(DATE_FILE) > 0:
        date = open(DATE_FILE, 'r', encoding="utf-8")
        date_diff = datetime.now() - parser.parse(date)
        print(date_diff)
        if date_diff.days >= 2:
            create_date_file(date)
            return True
        else:
            return False
    else:
        date_now = datetime.now()
        create_date_file(date_now)
        return True


def create_date_file(date):
    file = open(DATE_FILE, 'w', encoding="utf-8")
    print(date, file=open(DATE_FILE, 'a'))
    file.close()