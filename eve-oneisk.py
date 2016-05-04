#! python3

import os
import glob
import pyperclip

# Get the last imported file based on modified/creation date.
newest = max(glob.iglob('/home/cgar/Documents/EVE/logs/Marketlogs/*'), 
        key=os.path.getctime)
