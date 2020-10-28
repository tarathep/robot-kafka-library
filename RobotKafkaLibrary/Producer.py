from kafka import KafkaProducer

def Publish(broker,topic,message):
    try:
         producer = KafkaProducer(bootstrap_servers=broker)
         future = producer.send(topic,bytes(message,'utf-8'))
         future.get(timeout=60)
         return 'success'
    except:
        return 'err'