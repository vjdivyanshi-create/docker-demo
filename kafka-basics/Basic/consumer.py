from kafka import KafkaConsumer
import json

Consumer = KafkaConsumer(
    "demo-topic",
    bootstrap_servers = "kafka:9092",
    auto_offset_reset="earliest",
    value_deserializer = lambda x: json.loads(x.decode("utf-8"))
)

for msg in Consumer:
    print(msg.value)
    