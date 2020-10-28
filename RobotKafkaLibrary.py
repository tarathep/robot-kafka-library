from kafka import KafkaConsumer, KafkaProducer

def Consumer(broker,topic,timeout=3000):
    consumer = KafkaConsumer(bootstrap_servers=broker,auto_offset_reset='earliest',enable_auto_commit=True,
                         auto_commit_interval_ms=1000, group_id='robot-test',consumer_timeout_ms=timeout)
    consumer.subscribe([topic])

    for message in (consumer):
        consumer.commit()
        return (message[6].decode("utf-8"))
   

def Producer(broker,topic,message):
    try:
         producer = KafkaProducer(bootstrap_servers=broker)
         future = producer.send(topic,bytes(message,'utf-8'))
         future.get(timeout=60)
    except:
        return 'err'

   
# if __name__ == "__main__":
#     print(Producer('10.138.38.60:9092','foobarx','mimi'))
#     print(Consumer('10.138.38.65:9092','foobarx'))