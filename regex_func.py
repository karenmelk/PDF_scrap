import re

def upper_case(text):
    return bool(re.match(r'^[A-Z]+$',text))
def lower_case(text):
    return bool(re.match(r'^[a-z]+$',text))
def date_case(text):
    return bool(re.match(r'^\d+\.\d+\.\d+$',text))
def po(text):
    return bool(re.match(r'^[A-Z]\d+$',text))
def digits(text):
    return bool(re.match(r'\d+',text))