import requests
import mysql.connector
from tabulate import tabulate
from project3 import send_text_message


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

    # -------- SELECT ONLY 5 ROWS --------
    cursor.execute("""
        SELECT id, symbol, company_name
        FROM companies
        LIMIT 5
    """)

    rows = cursor.fetchall()

    headers = ["ID", "Symbol", "Company Name"]

    table_text = tabulate(rows, headers=headers, tablefmt="grid")

    print(table_text)

    # -------- SEND ONLY 5 TO VIBER --------
    send_text_message(table_text)

    cursor.close()
    conn.close()

else:
    print("Request Failed")