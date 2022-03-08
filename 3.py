import pandas as pd
from sqlalchemy import create_engine
import logging

# creating engine
engine = create_engine("postgresql+psycopg2://postgres:naresh#@localhost:5432/assignment")


def read_sheets(data, file):
    try:
        # reading the desired sheet
        if (data == 'Problem2'):
            # converting sheet into dataframe
            df = pd.read_excel(file, 'Problem2')

            # converting dataframe into sql table
            df.to_sql(name='emp_total_compensation2', con=engine, if_exists='replace', index=False)

    except:
        logging.error("Couldn't create the table")
        print("ERROR.")

    finally:
        logging.info("SUCCESS")
        print("Successfully created the table from excel sheet.")


# calling the excel file
with pd.ExcelFile('2_excel.xlsx') as xls:
    for sheet_name in xls.sheet_names:
        read_sheets(sheet_name, xls)
