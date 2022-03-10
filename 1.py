import logging
import psycopg2
import pandas as pd


def problem_1(query):
    try:
        # connecting database to python
        conn = psycopg2.connect(database="assignment", user="postgres", password="naresh", host="localhost", port="5432")
        logging.info("Connecting to database...")
        print("Connected.")
        cur = conn.cursor()
        cur.execute(query)
        rows = cur.fetchall()
        employee_no = []
        employee_name = []
        manager = []

        # for row in rows:
        #     print(row)

        for row in rows:
            temp_list = list(row)
            employee_no.append(temp_list[0])
            employee_name.append(temp_list[1])
            manager.append(temp_list[2])

        # print(employee_no)
        # print(employee_name)
        # print(manager)

        # converting list into dataframe
        df = pd.DataFrame({'EmployeeNo': employee_no, 'EmployeeName': employee_name, 'Manager': manager})
        # df_reset = df.set_index('EmployeeNo')
        print(df)

        # writing the dataframe into an excel file
        writer = pd.ExcelWriter('/Users/naresh/Downloads/1_excel.xlsx')
        df.to_excel(writer, sheet_name='Problem1', index=False)
        writer.save()

    except:
        logging.error("Couldn't connect to the database.")

    finally:
        logging.info("Closing database connection.")
        conn.close()
        print("Connection closed.")


if __name__ == "__main__":
    query = "SELECT empno as EmployeeNo, ename as EmployeeName, mgr as Manager FROM emp;"
    problem_1(query)
