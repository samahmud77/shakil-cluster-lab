FROM rabbitmq:3.13-management
LABEL maintainer = "Shakil Mahmud <shakil.mahmud@konasl.com>"

USER root
RUN apt-get update && apt install -y curl gnupg unzip

COPY ./rabbitmq_delayed_message_exchange-3.13.0.ez /opt/rabbitmq/plugins
COPY ./advance.config /etc/rabbitmq/rabbitmq.config

RUN rabbitmq-plugins enable --offline rabbitmq_delayed_message_exchange
ENV RABBITMQ_DEFAULT_USER=admin \
    RABBITMQ_DEFAULT_PASS=admin123 \
    RABBITMQ_DEFAULT_VHOST=/ \
    RABBITMQ_ERLANG_COOKIE=MY_SECRET_COOKIE

EXPOSE 15672 5672

CMD ["rabbitmq-server"]
