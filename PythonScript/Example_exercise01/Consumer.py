
from confluent_kafka import Consumer

running = True

def basic_consume_loop(c, topics):
    try:
        c.subscribe(topics)

        while running:
            msg = c.poll(timeout=1.0)
            if msg is None: continue

            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    # End of partition event
                    sys.stderr.write('%% %s [%d] reached end at offset %d\n' %
                                     (msg.topic(), msg.partition(), msg.offset()))
                elif msg.error():
                    raise KafkaException(msg.error())
            else:
                print(str(msg.value().decode()))
    finally:
        # Close down consumer to commit final offsets.
        c.close()

def shutdown():
    running = False

c = Consumer({'bootstrap.servers':'localhost:8097',
              'group.id':'group1',
			  'auto.offset.reset':'earliest'})
              
basic_consume_loop(c,['randomTopic'])