import mysql.connector
from datetime import datetime, timedelta
import json
import mysql_config

def get_one_keyword(conn):
    cursor = conn.cursor()
    query = f"SELECT keyword_id, keyword, date_start_end FROM {mysql_config.keyword_table} WHERE is_finish = 0 ORDER BY chatgpt_date_id DESC LIMIT 1"
    cursor.execute(query)
    result = cursor.fetchone()
    if result:
        data = {
            "keyword_id": result[0],
            "keyword": result[1],
            "date_start_end": result[2]
        }
        return data
    return None

def mark_keyword_finished(conn, keyword_id):
    cursor = conn.cursor()
    query = f"UPDATE {mysql_config.keyword_table} SET is_finish = 1 WHERE keyword_id = %s"
    cursor.execute(query, (keyword_id,))
    conn.commit()

def insert_keywords(keywords):
    # Database connection configuration
    config = {
        'user': mysql_config.user,
        'password': mysql_config.password,
        'host': mysql_config.host,
        'database': mysql_config.database,
    }

    # List of keywords
    keywords = [
        "Driverless Car", "Driverless SUV", "Driverless Vehicle", "Driverless Automobile",
        "Driverless Bus", "Driverless Truck", "Driverless Van", "Driverless Motor Vehicle",
        "Driverless Vehicle Technology", "Driverless Transport", "Without A Driver Car",
        "Without A Driver SUV", "Without A Driver Vehicle", "Without A Driver Automobile",
        "Without A Driver Bus", "Without A Driver Truck", "Without A Driver Van",
        "Without A Driver Motor Vehicle", "Without A Driver Vehicle Technology",
        "Without A Driver Transport", "No Driver Car", "No Driver SUV", "No Driver Vehicle",
        "No Driver Automobile", "No Driver Bus", "No Driver Truck", "No Driver Van",
        "No Driver Motor Vehicle", "No Driver Vehicle Technology", "No Driver Transport",
        "No Human Car", "No Human SUV", "No Human Vehicle", "No Human Automobile",
        "No Human Bus", "No Human Truck", "No Human Van", "No Human Motor Vehicle",
        "No Human Vehicle Technology", "No Human Transport", "No Operator Car",
        "No Operator SUV", "No Operator Vehicle", "No Operator Automobile", "No Operator Bus",
        "No Operator Truck", "No Operator Van", "No Operator Motor Vehicle",
        "No Operator Vehicle Technology", "No Operator Transport", "Unmanned Car",
        "Unmanned SUV", "Unmanned Vehicle", "Unmanned Automobile", "Unmanned Bus",
        "Unmanned Truck", "Unmanned Van", "Unmanned Motor Vehicle", "Unmanned Vehicle Technology",
        "Unmanned Transport", "Uncrewed Car", "Uncrewed SUV", "Uncrewed Vehicle",
        "Uncrewed Automobile", "Uncrewed Bus", "Uncrewed Truck", "Uncrewed Van",
        "Uncrewed Motor Vehicle", "Uncrewed Vehicle Technology", "Uncrewed Transport",
        "Autonomous Car", "Autonomous SUV", "Autonomous Vehicle", "Autonomous Automobile",
        "Autonomous Bus", "Autonomous Truck", "Autonomous Van", "Autonomous Motor Vehicle",
        "Autonomous Vehicle Technology", "Autonomous Transport", "Self-Driving Car",
        "Self-Driving SUV", "Self-Driving Vehicle", "Self-Driving Automobile", "Self-Driving Bus",
        "Self-Driving Truck", "Self-Driving Van", "Self-Driving Motor Vehicle",
        "Self-Driving Vehicle Technology", "Self-Driving Transport", "Self Drive Car",
        "Self Drive SUV", "Self Drive Vehicle", "Self Drive Automobile", "Self Drive Bus",
        "Self Drive Truck", "Self Drive Van", "Self Drive Motor Vehicle",
        "Self Drive Vehicle Technology", "Self Drive Transport", "Automated Car",
        "Automated SUV", "Automated Vehicle", "Automated Automobile", "Automated Bus",
        "Automated Truck", "Automated Van", "Automated Motor Vehicle",
        "Automated Vehicle Technology", "Automated Transport", "Computer Driven Car",
        "Computer Driven SUV", "Computer Driven Vehicle", "Computer Driven Automobile",
        "Computer Driven Bus", "Computer Driven Truck", "Computer Driven Van",
        "Computer Driven Motor Vehicle", "Computer Driven Vehicle Technology",
        "Computer Driven Transport", "Computer Controlled Car", "Computer Controlled SUV",
        "Computer Controlled Vehicle", "Computer Controlled Automobile", "Computer Controlled Bus",
        "Computer Controlled Truck", "Computer Controlled Van", "Computer Controlled Motor Vehicle",
        "Computer Controlled Vehicle Technology", "Computer Controlled Transport",
        "Robot Car", "Robot SUV", "Robot Vehicle", "Robot Automobile", "Robot Bus",
        "Robot Truck", "Robot Van", "Robot Motor Vehicle", "Robot Vehicle Technology", "Robot Transport"
    ]

    try:
        # Establish database connection
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()

        # Insert statement (using parameterized query to prevent SQL injection)
        insert_query = f"""
            INSERT INTO {mysql_config.keyword_table} (keyword, date_start_end, is_finish)
            VALUES (%s, %s, %s)
        """

        # Insert each keyword
        for keyword in keywords:
            cursor.execute(insert_query, (keyword, "until:2024-10-01 since:2024-09-02", 0))

        # Commit the transaction
        connection.commit()

        print("All keywords have been successfully inserted.")

    except mysql.connector.Error as err:
        print(f"Database error: {err}")

    finally:
        # Close cursor and connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()


# Uncomment the following line to create date information in the database table
# createDate()
