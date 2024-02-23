# Kafka sandbox ( by Docker )

**GOAL :** <br>
> Learning real-time streaming with Kafka.

# Framework

![Personal visualization - Kafka](https://github.com/HikariJadeEmpire/Kafka_SandBox_byDocker/assets/118663358/888a5eab-2be1-406c-a4b0-beb394fe7756)

# References commands

Build environment

```bash

docker-compose up --build

```

Create Topics through Docker :

```bash

docker exec broker kafka-topics --create --topic quickstart-avro-offsets --partitions 1 --replication-factor 1 --if-not-exists --zookeeper zookeeper:2181 \
&& docker exec broker kafka-topics --create --topic quickstart-avro-config --partitions 1 --replication-factor 1 --if-not-exists --zookeeper zookeeper:2181 \
&& docker exec broker kafka-topics --create --topic quickstart-avro-status --partitions 1 --replication-factor 1 --if-not-exists --zookeeper zookeeper:2181

```

Create this topic after define source connector :

```bash

docker exec broker kafka-topics --create --topic mykafka-customers --partitions 1 --replication-factor 1 --if-not-exists --zookeeper zookeeper:2181

```

Check Topics :

```bash

docker exec broker kafka-topics --describe --zookeeper zookeeper:2181 | grep -e mykafka-customers

```

Check Kafka connect :

```bash

docker logs kafka-connect | grep -e started

```

Check plug-ins :

```bash

curl -s -X GET http://localhost:8083/connector-plugins

```

# Source & Sink Connector

**SOURCE :** <br>
- [MySQL to MySQL](https://github.com/HikariJadeEmpire/Kafka_SandBox_byDocker/blob/main/KafkaJdbcConnect_mySql-mySql/source.json)
- [MySQL to HDFS](https://github.com/HikariJadeEmpire/Kafka_SandBox_byDocker/blob/main/KafkaJdbcConnect_mySql-HDFS/source.json)

**SINK :** <br>
- [MySQL to MySQL](https://github.com/HikariJadeEmpire/Kafka_SandBox_byDocker/blob/main/KafkaJdbcConnect_mySql-mySql/sink-mysql.json)
- [MySQL to HDFS](https://github.com/HikariJadeEmpire/Kafka_SandBox_byDocker/blob/main/KafkaJdbcConnect_mySql-HDFS/sink-hdfs.json)

<br>

Define source connector :

```bash

curl -d @"source.json" -H "Content-Type: application/json" -X POST http://localhost:8083/connectors

curl -s -X GET http://localhost:8083/connectors/quickstart-source/status
# For checking status

curl -X DELETE http://localhost:8083/connectors/quickstart-source

```

Define sink connector :

```bash

curl -d @"sink-mysql.json" -H "Content-Type: application/json" -X POST http://localhost:8083/connectors

curl -s -X GET http://localhost:8083/connectors/quickstart-sink/status
# For checking status

curl -X DELETE http://localhost:8083/connectors/quickstart-sink

```

# Docker references

Open container Terminal :

```bash

docker exec -it <container name> /bin/bash

```
