import pandas as pd


def read_csv_data():
    df = pd.read_csv("ExcelData.csv")
    print("I am reading the excel file!!!")
    print(df)

