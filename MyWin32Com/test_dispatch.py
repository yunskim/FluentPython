import win32com.client
import os

xl = win32com.client.Dispatch("Excel.Application")
xl.Application.Run(os.path.abspath("excelsheet.xlsm"))