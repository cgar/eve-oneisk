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

# Get the first value and substract one isk.
regex = re.compile(r'\d+.\d+')
result = regex.search(content_read)
if result:
	value = result.group()
	value = float(value)
	value = value - .01

pyperclip.copy(str(value))