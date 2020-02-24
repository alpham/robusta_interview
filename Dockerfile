FROM python:3.7

ARG env=prod

COPY . /opt/cipher
WORKDIR /opt/cipher

RUN chmod +x /opt/cipher/entrypoint.sh
RUN chmod +x /opt/cipher/cipher.py

RUN pip3 install -r requirements/$env.txt

ENTRYPOINT ["/opt/cipher/entrypoint.sh"]


# CMD python3 ./cipher.py --help
