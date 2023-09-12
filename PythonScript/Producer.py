#install 
# pip install confluent_kafka

# Producer
from confluent_kafka import Producer
import time

#######################################
# import mysql

import pymysql
import os
from dotenv import load_dotenv

load_dotenv()

# Connect to the database
connection = pymysql.connect(
                              host = os.getenv('MYSQL_HOST'),
                              port = int(os.getenv('MYSQL_PORT')),
                              user = os.getenv('MYSQL_USER'),
                              password = os.getenv('MYSQL_PASSWORD'),
                              db = os.getenv('MYSQL_DB'),
                              charset = os.getenv('MYSQL_CHARSET'),

                              cursorclass = pymysql.cursors.DictCursor
                              )

sql = "SELECT * FROM customers;"

with connection.cursor() as cursor:
  cursor.execute(sql)
  result = cursor.fetchall()

#########################################

p = Producer({'bootstrap.servers':'localhost:8097'})

def acked(err, msg):

    if err is not None:
        print("Failed to deliver message: %s: %s" % (str(msg), str(err)))
    else:
        print("Message produced: %s" % (msg.value().decode()))

for i,vl in enumerate(result):
    p.produce('ClassicModelsTopic', key=str(vl['customerNumber']), 
              value=' Name : '+str(vl['customerName'])+'    , Country : '+str(vl['country']), 
              callback=acked)
    time.sleep(1) # delay message for 1 second

    # Wait up to 1 second for events. Callbacks will be invoked during
    # this method call if the message is acknowledged.
    p.poll(1)