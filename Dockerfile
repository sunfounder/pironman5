FROM ubuntu:24.04

ARG VARIANT=base
ARG PIPOWER5=false

RUN apt-get update && apt-get install -y curl sudo util-linux git

# Ensure HOME and USER are set for the installer framework
RUN mkdir -p /root
ENV USER=root
ENV HOME=/root

# Copy entire repo for installer (needs overlays/, bin/, scripts/, etc.)
COPY . /root/pironman5
RUN cp /root/pironman5/install.sh /tmp/install.sh

RUN if [ "$PIPOWER5" = "true" ]; then \
        bash /tmp/install.sh --variant "$VARIANT" --container --pipower5; \
    else \
        bash /tmp/install.sh --variant "$VARIANT" --container; \
    fi

RUN rm -rf /tmp/install.sh

COPY docker-entrypoint.sh /
RUN chmod +x /docker-entrypoint.sh

EXPOSE 34001
CMD ["/docker-entrypoint.sh"]
