# read data from kafka topic
from kafka import KafkaConsumer, TopicPartition
import logging

topic = "topicname"

bootstrap_server = "yourbootstrapserver:9092"
sasl_mechanism = "PLAIN"
username = "username"
password = "password"
security_mechanism = "SASL_SSL"
group_id = "groupid"

consumer=KafkaCOnsumer(topic,
                      bootstrap_server=bootstrapserver,
                      auto_offset_reset='earliest',
                      security_protocol=security_protocol,
                      group_id=group_id,
                      sasl_mechanism = sasl_mechanism,
                      sasl_plain_username = username,
                      sasl_plain_password = password,
                      ssl_check_hostname = False,
                      fetch_max_wait_ms = 5000,
                      consumer_timeout_ms=60000)

i=0

#print one message
for msg in consumer:
  print(msg)
  i=i+1
  if(i==1):
    break

