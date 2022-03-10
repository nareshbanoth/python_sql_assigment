import psycopg2
import pandas as pd
import logging


def problem_2(query):
    try:

        # connecting to database
        conn = psycopg2.connect(database="assignment", user="postgres", password="naresh", host="localhost",
                                port="5432")
        logging.info("Connecting to database...")
        print("Connected.")
        cur = conn.cursor()

        # cleaning data and replacing null values to zeroes
        cur.execute("UPDATE jobhist SET enddate=CURRENT_DATE WHERE enddate IS NULL;")
        cur.execute("UPDATE jobhist SET comm=0 WHERE comm IS NULL;")

        cur.execute(query)
        rows = cur.fetchall()
        ename = []
        empno = []
        dname = []
        deptno = []
        total_compensation = []
        months_spent = []

        print(rows)
        for row in rows:
            temp_list = list(row)
            ename.append(temp_list[0])
            empno.append(temp_list[1])
            dname.append(temp_list[2])
            deptno.append(temp_list[3])
            total_compensation.append(temp_list[4])
            months_spent.append(temp_list[5])

        # creating dataframe
        df = pd.DataFrame({'EmployeeName': ename, 'EmployeeNo': empno, 'DepartmentName': dname, 'DepartmentNo':deptno,
                           'TotalCompensation': total_compensation, 'MonthsSpent': months_spent})

        writer = pd.ExcelWriter('/Users/naresh/Downloads/2_excel.xlsx')

        # converting the dataframe to excel
        df.to_excel(writer, sheet_name='Problem2', index=False)
        writer.save()

    except:
        logging.error("Couldn't connect to the database.")

    finally:
        logging.info("Closing database connection.")
        conn.close()
        print("Connection closed.")


if __name__ == "__main__":
    query = "SELECT emp.ename, jh.empno, dept.dname, jh.deptno, ROUND((((jh.enddate-jh.startdate)/30*jh.sal)+jh.comm),0) AS Total_compensation, ROUND((jh.enddate-jh.startdate)/30,0) AS Months_Spent FROM jobhist jh INNER JOIN dept ON jh.deptno = dept.deptno INNER JOIN emp ON jh.empno = emp.empno;"
    problem_2(query)
