#!/usr/bin/python3

from openpyxl import Workbook

wb = Workbook()

month = input("Welcome to my expense tracker. What month would you like to track the expense? ")

dest_filename = month + ".xlsx"

wb.save(filename=dest_filename)
