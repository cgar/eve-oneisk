#! python3

import os
import re
import glob
import pyperclip

# Get the last imported file based on modified/creation date.
newest = max(glob.iglob('/home/cgar/Documents/EVE/logs/Marketlogs/*'), 
        key=os.path.getctime)

# Open and read the latest file in read mode.
content = open(newest, 'r')
content_read = content.read()

regex = re.compile(r'\d+.\d+')
result = regex.search(content_read)
print(result.group())


# def get_first_nbr_from_file(input_file):