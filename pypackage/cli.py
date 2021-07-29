# -*- coding: utf-8 -*-
import requests

def execute():
    print("execute command.")
    response = requests.get('https://www.google.com/')
    print(response.status_code)