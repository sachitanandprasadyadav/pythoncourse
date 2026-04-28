import requests
import mysql.connector
from tabulate import tabulate


url = "https://merolagani.com/handlers/AutoSuggestHandler.ashx?type=Company"

r = requests.get(url)

if r.status_code == 200:

    # Database connection
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="sachin@@@123",
        database="nepal_stock"
    )

    cursor = conn.cursor()

    # -------- SELECT DATA FROM DATABASE --------
    cursor.execute("SELECT id, symbol, company_name FROM companies")

    rows = cursor.fetchall()

    # Print in table format
    headers = ["ID", "Symbol", "Company Name"]

    print(tabulate(rows, headers=headers, tablefmt="grid"))

    cursor.close()
    conn.close()

else:
    print("Request Failed")