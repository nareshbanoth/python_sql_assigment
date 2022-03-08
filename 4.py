import pandas as pd
from sqlalchemy import create_engine
import logging

# creating engine
engine = create_engine("postgresql+psycopg2://postgres:naresh#@localhost:5432/assignment")


def read_sheets(data, file):
    try:
        if data == 'Problem2':
            # converting excel into a dataframe
            df = pd.read_excel(file, 'Problem2')
            return df

    except:
        logging.error("Error")
        print("sorry count return df.")

    finally:
        logging.info("SUCCESS")
        print("Successfully executed.")


with pd.ExcelFile('Problem_2_excel.xlsx') as xls:
    for sheet_name in xls.sheet_names:
        new_df = read_sheets(sheet_name, xls)



temp1_df = new_df.groupby(['DepartmentName', 'DepartmentNo']).agg(
    Total_Compensation=pd.NamedAgg(column='TotalCompensation', aggfunc="sum")
).reset_index()

# applying group by deptno, deptname and adding the compensation on the dataframe we converted from the excel sheet
print(temp1_df)


# converting this newly created dataframe into excel
writer = pd.ExcelWriter('/Users/naresh/Downloads/4_excel.xlsx')
temp1_df.to_excel(writer, sheet_name='Problem4', index=False)
writer.save()
