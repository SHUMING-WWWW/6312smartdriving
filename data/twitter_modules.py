import time
import requests
import data_insert
import keyword_tools
import mysql.connector
import os
import mysql_config
from datetime import datetime, timedelta

def insert_to_mysql(entries_data, keyword, date_start_end, conn):
    for entry in entries_data:
        if entry["entryId"].startswith("tweet"):
            try:
                data_insert.insert_data_to_mysql(entry, keyword, date_start_end, conn)
                print("Tweet data inserted into the database.")
            except:
                print("Error encountered while inserting one entry.")
                continue
        else:
            print("Not a tweet entry, skipping.")
            continue

def spider_thread():
    print("Starting the spider...")
    time.sleep(1)
    while True:
        os.system("cls")  # Clear console output
        conn = mysql.connector.connect(
            host=mysql_config.host,
            user=mysql_config.user,
            password=mysql_config.password,
            database=mysql_config.database
        )
        # Retrieve keyword information
        date_json = keyword_tools.get_one_keyword(conn)
        date_start_end = date_json['data_start_end']
        keyword = date_json['keyword']
        keyword_id = date_json['keyword_id']
        # Mark the keyword as finished
        keyword_tools.mark_keyword_finished(conn, keyword_id)

        print(f"Starting to scrape keyword ID {keyword_id}, keyword: {keyword}, time range: {date_start_end}.")
        search_term = f"{keyword} lang:en {date_start_end}"

        url = f"https://api URL/{search_term}"

        querystring = {
            'category': 'Latest',
            'count': 20,
            'cursor': ''
        }

        headers = {
            "x-api-key": "",  # API key
            "x-api-host": "your api host"  # API host
        }

        response = requests.get(url, headers=headers, params=querystring)
        entries = response.json().get("entries")[0].get("entries")
        bottom_cursor = entries[-1].get("content").get("value")
        insert_to_mysql(entries, keyword, date_start_end, conn)

        page_number = 1
        print(f"Scraping page {page_number}.")
        print(f"Page {page_number} retrieved {len(entries)} entries.")
        print(f"Bottom cursor token: {bottom_cursor}")

        while True:
            page_number += 1
            print(f"Scraping page {page_number}.")
            querystring['cursor'] = bottom_cursor

            response = requests.get(url, headers=headers, params=querystring)
            entries_tree = response.json().get("entries")
            
            try:
                entries_bottom = entries_tree[-1]
            except Exception as e:
                print("Unknown error, retrying...")
                page_number -= 1
                continue

            entries = entries_tree[0].get("entries")

            try:
                insert_to_mysql(entries, keyword, date_start_end, conn)
            except:
                print("All data within the time range has been scraped.")
                break

            try:
                print(f"Page {page_number} retrieved {len(entries)} entries.")
            except:
                print("All data within the time range has been scraped.")
                break

            bottom_cursor = entries_bottom.get("entry").get("content").get("value")
            print(f"Bottom cursor token: {bottom_cursor}")

        conn.disconnect()
