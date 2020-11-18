import os,os.path as pth
import datetime

from os import DirEntry
fl = open("C:\\ProgramData\\Automation\\SOAR\\Calling_Campaigns\\Calling_Cmpgn_Template.xlsm")
print(datetime.datetime.today().weekday() )
"""
with os.scandir() as dir_entries:
    for entry in dir_entries:
        for itm in entry.__all__:
            #info = entry.stat()
            print(itm)
"""
#path = "\\\\Plswe224\\filestream\\SOAR\\Files\\Apr_May2020_AAL.xlsx"
#path = "C:\\ProgramData\\Automation\\SOAR\\Calling_Campaigns\\Calling_Cmpgn_Template.xlsm"


#print(io.open(path, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True))