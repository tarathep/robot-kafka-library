from kafka import KafkaConsumer

def Subcribe(broker,topic,timeout=3000):
    consumer = KafkaConsumer(bootstrap_servers=broker,auto_offset_reset='earliest',enable_auto_commit=True,
                         auto_commit_interval_ms=1000, group_id='robot-test',consumer_timeout_ms=timeout)
    consumer.subscribe([topic])

    for message in (consumer):
        consumer.commit()
        return (message[6].decode("utf-8"))
    return 'err'