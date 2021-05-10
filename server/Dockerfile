FROM python:alpine
RUN apk add vim strace ltrace tcpdump curl
COPY server.py .
CMD [ "python", "server.py" ]