# print("Test")
# x = 10
# y = "adasdad"
# try:
#     value = x < 10
# except:
#     print("not allowed")
# else:
#     print("else")
# finally:
#     print("finally")

# try:
#     if x < 10:
#         print("Below")
#     elif x > 10:
#         print("Above")
#     else:
#         print("Wata")
# except:
#     print("may mali")

# list1 = [1, 2, 3, 4, 5]
# list2 = [2, 3, 4]

# list3 = [list1, list2]

# for i in list3:
#     for z in i:
#         print(z)

# list4 = [z for i in list3 for z in i]
# print(list4)

# testStr = "I am a test string %s, test number %i" % ("Lex", 123)
# print(testStr)

# testDict = { "name": "Lex", "age": 12 }
# testDictString = "I am {name}, and I am {age} years old".format(**testDict)
# print(testDictString)

# print("--------------------")

# fileTxt = open("sample.txt", "r")
# dataHandle = fileTxt.read()
# print(dataHandle)
# fileTxt.close()

# print("--------------------")

# fileTxt2 = open("sample.txt", "r")
# dataHandleLine = fileTxt2.readline()
# print(dataHandleLine)
# fileTxt2.close()

# print("--------------------")

# fileTxt3 = open("sample.txt", "r")
# dataHandleLines = fileTxt3.readlines()
# print(dataHandleLines)
# fileTxt3.close()

# print("--------------------")

# with open("sample.txt") as fileHandler:
#     for line in fileHandler:
#         print(line)

# from math import sqrt, pi
# sqrt = sqrt(5)
# print(sqrt)


# # import this

# def a_function():
#     try:
#         print("I am printing" + x)
#     except:
#         print("not doable")

# a_function()

# def empty_function():
#     pass

# def add(a, b):
#     return a + b

# def substract(a, b):
#     return a - b

# def multiply(a, b):
#     return a * b

# def divide(a, b):
#     return a / b

# def mod(a, b):
#     return a % b

# print(add(99, 2))
# print(substract(99, 2))
# print(multiply(99, 2))
# print(divide(99, 2))
# print(mod(99, 2))

# addWithString = "Add result %i" % add(99,2)
# print(addWithString)

# substractionWithString = "Substraction result %i" % substract(99,2)
# print(substractionWithString)

# multiplicationWithString = "Multiply result %i" % multiply(99,2)
# print(multiplicationWithString)

# divideWithString = "Divide result %i" % divide(99,2)
# print(divideWithString)

# modWithString = "Mod result %i" % mod(99,2)
# print(modWithString)

# # pandas codes
# import pandas as pd

# data = pd.read_excel('sample.xlsx')
# # To read the sheet named 'Sheet1'.
# # data = pd.read_excel('file_path.xlsx', sheet_name='Sheet1')

# # To read the sheet at index 0 (the first sheet).
# # data = pd.read_excel('file_path.xlsx', sheet_name=0)

# print(data.head())

# xlsxHeaders = pd.DataFrame(data.head())
# for xlsxHeader in xlsxHeaders:
#     print(xlsxHeader)

# print(xlsxHeaders.columns)

# for i, row in data.iterrows():
#     print(i) # row index
#     for col in xlsxHeaders.columns:
#         print(row[col]) # getting cell value

# # try comprehension approach
# # row[col]
# rowCol = [i for i, row in data.iterrows() for col in xlsxHeaders.columns]
# print(rowCol)

# # Function args difference
# # *args -> list
# # **args -> object

# # Google Sheets Reading
# import gspread
# from oauth2client.service_account import ServiceAccountCredentials

# scopes = [
#     'https://www.googleapis.com/auth/spreadsheets',
#     'https://www.googleapis.com/auth/drive'
# ]

# creds = ServiceAccountCredentials.from_json_keyfile_name("sample-key.json", scopes=scopes)

# file = gspread.authorize(creds)
# workbook = file.open("MAP")
# sheet = workbook.sheet1

# for cell in sheet.range('A2:C5'):
#     print(cell.value)

# print(sheet.cell(4,3).value)
# print(sheet.row_values(4))
# print(sheet.col_values(3))

# # Google Sheet Update
# sheet.update_acell('A2', 'IVY')
# print(sheet.cell(2,1).value)
# if sheet.cell(2,1).value == "TEST":
#     sheet.update('A5:C5',[['Test', 31, 'Lorem Ipsum']])

# MySQL Connection

# try:
    # This is from the sample I read
    # with connect(
    #     host="localhost",
    #     user="root",
    #     password="secret",
    #     database="camden_map"
    # ) as connection:
    #     with connection.cursor() as cursor:
    #         # Select Statement
    #         select_records = "SELECT * FROM credit_score_merged LIMIT 1;"
    #         cursor.execute(select_records)
    #         for row in cursor.fetchall():
    #             # print(row[1]) # Can be used per index, usuable when returned all fields and get specific index of the response
    #             for x in row:
    #                 print(x) # print all data inside the row

    # This is my own approach without using WITH
#     connection = connect(
#         host="localhost",
#         user="root",
#         password="secret",
#         database="camden_map"
#     )
#     select_records = "SELECT * FROM credit_score_merged LIMIT 1;"
#     cursor = connection.cursor()
#     cursor.execute(select_records)
#     # print(cursor.fetchall())
# except Error as e:
#     print(e)

# This is my own approach without using Class!
from getpass import getpass
from mysql.connector import connect, Error
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import time
class Process():

    def __init__(self):
        self.connection = Process.db_connection()

    def db_connection():
        return connect(
            host="localhost",
            user="root",
            password="secret",
            database="camden_map"
        )
    
    def count_records():
        try:
            connection = Process.db_connection()
            count_records = "SELECT count(*) as count FROM credit_score_merged"
            cursor = connection.cursor()
            cursor.execute(count_records)
            return cursor.fetchone()[0]
        except Error as e:
            print(e)

    def select_records(limitstart = 0):
        try:
            connection = Process.db_connection()
            select_records = """SELECT
                property_no,
                lease_id,
                market,
                building,
                area,
                (CASE
					WHEN floor = "Basement" THEN "-1"
					WHEN floor = "Ground" THEN "0"
					WHEN floor = "1st" THEN "1"
					WHEN floor = "2nd" THEN "2"
					WHEN floor = "3rd" THEN "3"
					WHEN floor = "1st & 2nd" THEN "1 & 2"
					WHEN floor = "2nd & 3rd" THEN "2 & 3"
					WHEN floor = "Grd & 1st" THEN "G & 1"
					WHEN floor = "Grd to 1st" THEN "G to 1"
					WHEN floor = "Grd to 2nd" THEN "G to 2"
					WHEN floor = "Grd to 3rd" THEN "G to 3"
                    ELSE "-"
				END) AS floor,
                unit_no,
                planned_usage,
                tenant_ref,
                trading_as,
                tenant,
                tenant_category,
                net_area,
                contracted_rent_pa,
                IFNULL(credit_score, 0) AS credit_score,
                IFNULL(passing_rent_pa, 0) AS passing_rent_pa,
                IFNULL(social_impact_score, 0) AS social_impact_score,
                bp_code,
                bp_name,
                bp_combined_code_name,
                IFNULL(status_creditsafe, 0) AS status_creditsafe
            FROM
                credit_score_merged LIMIT %s, 2""" % (limitstart)
            cursor = connection.cursor(dictionary=True)
            cursor.execute(select_records)
            return cursor.fetchall()
        except Error as e:
            print(e)
    
    def select_records_by_leaseid(leaseid):
        try:
            connection = Process.db_connection()
            select_records = "SELECT * FROM credit_score_merged WHERE lease_id = %i;" % leaseid
            cursor = connection.cursor()
            cursor.execute(select_records)
            print(cursor.fetchall())
        except Error as e:
            print(e)

    def update_record_by_leaseid(leaseid):
        try:
            connection = Process.db_connection()
            update_records = """UPDATE credit_score_merged SET tenant = '%s' WHERE lease_id = %i;""" % (
                "Sample Information Updates",
                leaseid
            )
            cursor = connection.cursor()
            cursor.execute(update_records)
            connection.commit()
        except Error as e:
            print(e)
        
    def import_table_to_sheets():
        try:

            # Google Sheets Reading
            scopes = [
                'https://www.googleapis.com/auth/spreadsheets',
                'https://www.googleapis.com/auth/drive'
            ]

            creds = ServiceAccountCredentials.from_json_keyfile_name("sample-key.json", scopes=scopes)

            file = gspread.authorize(creds)
            workbook = file.open("Data Map Information")
            # workbook = file.open("MAP") # My very own workbook
            sheet = workbook.sheet1

            sheet.update('W1:Z1',[['BP Code', 'BP Name', 'BP Combined', 'Status Credit Safe']])

            limit = 0
            recCounter = int(Process.count_records())
            rowCounter = 2
            while limit <= recCounter:
                records = Process.select_records(limit)

                # lopp the contents display and insert into google sheet
                for value in records:
                    # print(rowCounter)

                    # script to insert records to google sheet
                    # Google Sheet Update
                    sheet.update_acell('A' + str(rowCounter), str(value["property_no"]))
                    sheet.update_acell('B' + str(rowCounter), str(value["lease_id"]))
                    sheet.update_acell('D' + str(rowCounter), value["market"].title())
                    sheet.update_acell('E' + str(rowCounter), value["building"])
                    sheet.update_acell('F' + str(rowCounter), value["area"])
                    sheet.update_acell('G' + str(rowCounter), value["floor"])
                    sheet.update_acell('H' + str(rowCounter), value["unit_no"])
                    sheet.update_acell('K' + str(rowCounter), value["planned_usage"])
                    sheet.update_acell('L' + str(rowCounter), value["tenant_ref"])
                    sheet.update_acell('M' + str(rowCounter), value["trading_as"])
                    sheet.update_acell('N' + str(rowCounter), value["tenant"])
                    sheet.update_acell('O' + str(rowCounter), value["tenant_category"])
                    sheet.update_acell('Q' + str(rowCounter), value["net_area"])
                    sheet.update_acell('R' + str(rowCounter), value["contracted_rent_pa"])
                    sheet.update_acell('S' + str(rowCounter), value["credit_score"])
                    sheet.update_acell('T' + str(rowCounter), value["passing_rent_pa"])
                    sheet.update_acell('U' + str(rowCounter), value["social_impact_score"])
                    sheet.update_acell('W' + str(rowCounter), value["bp_code"])
                    sheet.update_acell('X' + str(rowCounter), value["bp_name"])
                    sheet.update_acell('Y' + str(rowCounter), value["bp_combined_code_name"])
                    sheet.update_acell('Z' + str(rowCounter), value["status_creditsafe"])

                    rowCounter += 1

                limit += 2
                print("limit")
                print(limit)
                print("rowCounter")
                print(rowCounter)
                print("recCounter")
                print(recCounter)
                time.sleep(70)
                print("slept for 70 seconds")
        except Error as e:
            print(e)


# Process.select_records_by_leaseid(12477)
# print("\n\n\n Update the details")
# Process.update_record_by_leaseid(12477)

Process.import_table_to_sheets()
# Goal for today
# Spreadsheet populate the data!
# loop the data
# check the spreadsheet data and update the data

# update? or remove and repopulate



#Darkwear UK Limited
# connection = Process.db_connection()
# select_records = "SELECT * FROM credit_score_merged LIMIT 1;"
# cursor = connection.cursor()
# cursor.execute(select_records)
# print(cursor.fetchall())

# property_no
# lease_id
# market
# building
# area
# floor
# unit_no
# planned_usage
# tenant_ref
# trading_as
# tenant
# tenant_category
# net_area
# contracted_rent_pa
# credit_score
# passing_rent_pa
# social_impact_score

# A
# B
# D
# E
# F
# G
# H
# K
# L
# M
# N
# O
# Q
# R
# S
# T
# U

# cell_ranges_and_values = {
#     'A' + str(rowCounter): str(value["property_no"]),
#     'B' + str(rowCounter): str(value["lease_id"]),
#     'D' + str(rowCounter): value["market"].title(), 
#     'E' + str(rowCounter): value["building"], 
#     'F' + str(rowCounter): value["area"], 
#     'G' + str(rowCounter): value["floor"], 
#     'H' + str(rowCounter): value["unit_no"], 
#     'K' + str(rowCounter): value["planned_usage"], 
#     'L' + str(rowCounter): value["tenant_ref"], 
#     'M' + str(rowCounter): value["trading_as"], 
#     'N' + str(rowCounter): value["tenant"], 
#     'O' + str(rowCounter): value["tenant_category"], 
#     'Q' + str(rowCounter): value["net_area"], 
#     'R' + str(rowCounter): value["contracted_rent_pa"], 
#     'S' + str(rowCounter): value["credit_score"], 
#     'T' + str(rowCounter): value["passing_rent_pa"], 
#     'U' + str(rowCounter): value["social_impact_score"], 
# }

# # Create a list of Cell objects
# cell_list = []
# for cell_range, new_value in cell_ranges_and_values.items():
#     cell = gspread.models.Cell(row=sheet.range(cell_range)[0].row,
#                             col=sheet.range(cell_range)[0].col,
#                             value=new_value)
#     cell_list.append(cell)

# # Update the specified cell ranges with the new data
# sheet.update_cells(cell_list)

# - Headings String - #
# Property Number
# Lease ID (This is unique)
# Market
# Building
# Area
# Floor
# Unit Number
# Type
# Planned Usage
# Net Area
# ERV
# Unit Status
# Tenant Ref
# Tenant
# Trading As
# Tenant Sector
# Tenant Category
# Lease Status
# Least Type
# Service Charge
# Rent Fee
# Contracted Rent
# Passing Rent
# CR - PR
# Passing Rent Rate
# Passing Rent Comment
# Notes
# BP Code
# BP Name
# Foreign Name
# VAT Number
# Company Reg Number
# Quarter Social
# Building Social
# Unit Social
# Name Social
# Trading As Social
# Email
# IG
# IG Followers
# IG Engagements
# IG Posts
# IG Engagements Ratio
# FB
# FB Followers
# FB Engagements
# FB Posts
# FB Engagements Ratio
# TT
# TT Followers
# TT Posts Likes
# Tagged
# Requires Trader Page
# Notes Social
# Impact Score Social
# Credit Score
# Credit Status
# BP Combined Code Name