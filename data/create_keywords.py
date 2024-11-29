import mysql.connector

# Database connection configuration
config = {
    'user': 'root',
    'password': 'vgoushabi',
    'host': '43.136.25.137',
    'database': 'twitter_spider',
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

def insert_keywords(keywords):
    try:
        # Establish database connection
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()

        # Insert query (using parameterized query to prevent SQL injection)
        insert_query = """
            INSERT INTO customer_1022_date (date_start, date_end, is_finish)
            VALUES (%s, %s, %s)
        """

        # Insert each keyword
        for keyword in keywords:
            cursor.execute(insert_query, (keyword, keyword, 0))

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

# Execute the insert operation
insert_keywords(keywords)

