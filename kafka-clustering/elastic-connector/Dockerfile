FROM confluentinc/cp-kafka-connect:7.7.0

ENV CONNECT_PLUGIN_PATH="/usr/share/java,/usr/share/confluent-hub-components"

RUN confluent-hub install --no-prompt confluentinc/kafka-connect-elasticsearch:latest

EXPOSE 8083
