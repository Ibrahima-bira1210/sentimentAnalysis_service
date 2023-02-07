from flask import Flask, request
import psycopg2
from flask_ngrok import run_with_ngrok
from preprocess import preprocess
from sentiment import sentiment
from topic import get_Topic
import load_env as env

app = Flask(__name__)
run_with_ngrok(app)  # Start ngrok when app is run


@app.route('/getSentiment', methods=['GET'])
def get_sentiment():  # put application's code here
    data = request.get_json()
    word = data['word']
    clean_word = preprocess(word)
    return sentiment(clean_word)


@app.route('/getCleanText', methods=['GET'])
def get_cleanText():  # put application's code here
    data = request.get_json()
    word = data['word']
    return preprocess(word)


@app.route('/getTopic', methods=['GET'])
def get_topic():  # put application's code here
    data = request.get_json()
    word = data['word']
    clean_word = preprocess(word)
    return get_Topic(clean_word)


@app.route('/loadSentimentToDB', methods=['POST'])
def load_sentiment():  # put application's code here
    conn = psycopg2.connect(host=env.db_host, database=env.db_name, port=env.db_port, user=env.db_user,
                            password=env.db_passwd)
    cur = conn.cursor()
    # select all rows from TwitterTweet table
    cur.execute("SELECT * FROM TwitterTweet")
    rows = cur.fetchall()
    for row in rows:
        result = sentiment(preprocess(row))
        # insert result to sentiment column in TwitterTweet table
        cur.execute("UPDATE TwitterTweet SET sentiments = %s WHERE Tweet_Id = %s", (result, row[0]))

    # Commit the changes to the database
    conn.commit()

    # Close the cursor and connection
    cur.close()
    conn.close()

    return "load sentiment done"


@app.route('/loadTopicToDB', methods=['GET'])
def load_topic():  # put application's code here
    conn = psycopg2.connect(host=env.db_host, database=env.db_name, port=env.db_port, user=env.db_user,
                            password=env.db_passwd)
    cur = conn.cursor()
    # select all rows from TwitterTweet table
    cur.execute("SELECT * FROM TwitterTweet")
    rows = cur.fetchall()
    for row in rows:
        result = get_Topic(preprocess(row))
        # insert result to sentiment column in TwitterTweet table
        cur.execute("UPDATE TwitterTweet SET topics = %s WHERE Tweet_Id = %s", (result, row[0]))

    # Commit the changes to the database
    conn.commit()

    # Close the cursor and connection
    cur.close()
    conn.close()

    return "load topic done"


if __name__ == '__main__':
    app.run()
