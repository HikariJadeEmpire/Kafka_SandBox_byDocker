#install 
# pip install confluent_kafka

# Producer
from confluent_kafka import Producer
import time

p = Producer({'bootstrap.servers':'localhost:8097'})

def acked(err, msg):
    if err is not None:
        print("Failed to deliver message: %s: %s" % (str(msg), str(err)))
    else:
        print("Message produced: %s" % (msg.value().decode()))

i = 0
while i<10:
    p.produce('randomTopic', key="key", value="value"+str(i), callback=acked)
    time.sleep(1) # delay message for 1 second
    i+=1

    # Wait up to 1 second for events. Callbacks will be invoked during
    # this method call if the message is acknowledged.
    p.poll(1)