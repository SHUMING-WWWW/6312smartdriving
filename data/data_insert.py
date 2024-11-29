import json

def insert_data_to_mysql(data, keyword, date_start_end, conn):
    # Parse JSON data
    tweet = data['content']['itemContent']['tweet_results']['result']
    user = tweet['core']['user_results']['result']

    # Extract required fields
    twitter_id = tweet['rest_id']
    typename = tweet['__typename']
    user_rest_id = user['rest_id']
    user_name = user['legacy']['name']
    user_screen_name = user['legacy']['screen_name']
    user_followers_count = user['legacy']['followers_count']
    user_url = user['legacy'].get('profile_banner_url', None)
    full_text = tweet['legacy']['full_text']
    favorite_count = tweet['legacy']['favorite_count']
    bookmark_count = tweet['legacy']['bookmark_count']
    reply_count = tweet['legacy']['reply_count']
    retweet_count = tweet['legacy']['retweet_count']
    quote_count = tweet['legacy']['quote_count']
    lang = tweet['legacy']['lang']
    created_at = tweet['legacy']['created_at']

    cursor = conn.cursor()

    # Insert data
    insert_query = """
    INSERT INTO california_data (
        twitter_id, typename, user_rest_id, user_name, user_screen_name, 
        user_followers_count, user_url, full_text, favorite_count, bookmark_count, 
        reply_count, retweet_count, quote_count, created_at, lang, keyword, date_start_end
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(insert_query, (
        twitter_id, typename, user_rest_id, user_name, user_screen_name,
        user_followers_count, user_url, full_text, favorite_count, bookmark_count,
        reply_count, retweet_count, quote_count, created_at, lang, keyword, date_start_end
    ))

    # Commit the transaction
    conn.commit()

    # Close the connection
    cursor.close()
