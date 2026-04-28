# Import requests library to call API (get data from website)
import requests

# Import MySQL connector to connect Python with MySQL database
import mysql.connector




# API URL to get company list from Merolagani
url = "https://merolagani.com/handlers/AutoSuggestHandler.ashx?type=Company"

# Send GET request to API
r = requests.get(url)

# Check if request is successful (HTTP 200 = OK)
if r.status_code == 200:

    # Convert JSON response into Python list/dictionary
    result = r.json()

    # Connect to MySQL database
    conn = mysql.connector.connect(
        host="localhost",              # database server (local PC)
        user="root",                   # MySQL username
        password="sachin@@@123",       # MySQL password
        database="nepal_stock"         # database name
    )

    # Create cursor to execute SQL queries
    cursor = conn.cursor()

    # Loop through each company in API result
    for i in result:

        # Get company ID from API
        id = i['v']

        # Get stock symbol (like NABIL, NICA)
        symbol = i['d']

        # Get full company name
        company = i['l']

        # Insert data into MySQL table
        cursor.execute("""
            INSERT INTO companies (id, symbol, company_name)
            VALUES (%s, %s, %s)
        """, (id, symbol, company))

    # Save all changes into database
    conn.commit()

    

    # Print success message in terminal
    print("Data inserted successfully!")

    # Close cursor (free resources)
    cursor.close()

    # Close database connection
    conn.close()

# If API request fails
else:
    print("Request Failed")